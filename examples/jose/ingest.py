#!/usr/bin/env python3
import os
import sys
import argparse
import asyncio
import time
import logging
from pathlib import Path
from tqdm import tqdm

from lightrag import LightRAG
from lightrag.llm.openai import gpt_4o_mini_complete, gpt_4o_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger

# Available models
AVAILABLE_MODELS = {
    "gpt-4o-mini": gpt_4o_mini_complete,
    "gpt-4o": gpt_4o_complete,
}

# Define working directory for LightRAG
WORKING_DIR = "./jose_rag_storage"

# Supported file extensions
SUPPORTED_TEXT_EXTENSIONS = ['.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.csv', '.xml']

# Configure logging
logger = logging.getLogger("ingest")

def configure_logging(verbose=False):
    """Configure logging based on verbosity level."""
    log_level = logging.DEBUG if verbose else logging.INFO

    # Set up logging for LightRAG
    setup_logger("lightrag", level=log_level)

    # Set up logging for this script
    logger.setLevel(log_level)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(console_handler)

class FileIngestor:
    def __init__(self, file_path, model_name="gpt-4o-mini", verbose=False):
        """Initialize the file ingestor with the path to the file to ingest."""
        self.file_path = Path(file_path)
        self.verbose = verbose
        self.model_name = model_name

        # Validate model name
        if self.model_name not in AVAILABLE_MODELS:
            raise ValueError(f"Invalid model name: {self.model_name}. Available models: {', '.join(AVAILABLE_MODELS.keys())}")

        self.model_func = AVAILABLE_MODELS[self.model_name]

        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # Check if file type is supported
        if self.file_path.suffix.lower() not in SUPPORTED_TEXT_EXTENSIONS:
            logger.warning(f"File type {self.file_path.suffix} may not be supported. Proceeding anyway.")

        # Create working directory if it doesn't exist
        if not os.path.exists(WORKING_DIR):
            os.makedirs(WORKING_DIR)
            logger.debug(f"Created working directory: {WORKING_DIR}")

        self.rag = None
        self.content = None
        self.file_size = self.file_path.stat().st_size

        logger.debug(f"FileIngestor initialized for {self.file_path} ({self.file_size} bytes) using model {self.model_name}")

    async def initialize_rag(self):
        """Initialize the LightRAG instance with OpenAI model."""
        logger.info(f"Initializing LightRAG with working directory: {WORKING_DIR} and model {self.model_name}")

        self.rag = LightRAG(
            working_dir=WORKING_DIR,
            embedding_func=openai_embed,
            llm_model_func=self.model_func,
        )

        logger.debug("Initializing storages...")
        await self.rag.initialize_storages()
        await initialize_pipeline_status()

        logger.info("LightRAG initialized successfully")
        return self.rag

    def read_file_content(self):
        """Read the content of the file to ingest."""
        logger.info(f"Reading file: {self.file_path}")

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()

            content_length = len(self.content)
            logger.debug(f"Read {content_length} characters from file")

            # Log a preview of the content if in verbose mode
            if self.verbose and content_length > 0:
                preview_length = min(200, content_length)
                preview = self.content[:preview_length] + ("..." if content_length > preview_length else "")
                logger.debug(f"Content preview: {preview}")

            return self.content

        except UnicodeDecodeError:
            logger.error(f"Failed to read file as UTF-8 text: {self.file_path}")
            raise
        except Exception as e:
            logger.error(f"Error reading file: {e}")
            raise

    async def ingest_content(self):
        """Ingest the file content into LightRAG with progress bar."""
        if not self.content:
            self.read_file_content()

        if not self.rag:
            await self.initialize_rag()

        logger.info(f"Ingesting content from {self.file_path.name}")

        # Create a progress bar
        progress_bar = tqdm(
            total=100,
            desc="Ingesting content",
            unit="%",
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}% [{elapsed}<{remaining}]"
        )

        # Create a flag to signal when ingestion is complete
        ingestion_complete = asyncio.Event()

        # Define a callback to update progress
        async def progress_callback():
            # Initial progress steps
            for i in range(0, 50, 5):
                if ingestion_complete.is_set():
                    break
                progress_bar.update(5)
                logger.debug(f"Progress: {progress_bar.n}%")
                await asyncio.sleep(0.2)

            # Wait for ingestion to complete while showing progress
            while not ingestion_complete.is_set():
                # Slower progress as we approach completion
                progress_value = min(2, 100 - progress_bar.n)
                if progress_value > 0:
                    progress_bar.update(progress_value)
                    logger.debug(f"Progress: {progress_bar.n}%")
                await asyncio.sleep(0.5)

            # Ensure we reach 100%
            if progress_bar.n < 100:
                progress_bar.update(100 - progress_bar.n)
                logger.debug(f"Progress: 100%")

        # Start the progress callback in a separate task
        progress_task = asyncio.create_task(progress_callback())

        # Perform the actual ingestion
        start_time = time.time()
        try:
            logger.debug("Starting RAG insertion...")
            await self.rag.ainsert(
                self.content,
                file_paths=str(self.file_path)
            )
            logger.debug("RAG insertion completed")
            ingestion_complete.set()

            # Wait for the progress to complete
            await progress_task
            progress_bar.close()

            elapsed_time = time.time() - start_time
            logger.info(f"Successfully ingested content from {self.file_path.name} in {elapsed_time:.2f} seconds")

        except Exception as e:
            ingestion_complete.set()
            progress_bar.close()
            logger.error(f"Error during ingestion: {e}")
            raise

    async def finalize(self):
        """Finalize the LightRAG instance."""
        if self.rag:
            logger.debug("Finalizing LightRAG storages...")
            await self.rag.finalize_storages()
            logger.info("LightRAG instance finalized")

def display_file_info(file_path):
    """Display information about the file to be ingested."""
    path = Path(file_path)
    if not path.exists():
        logger.error(f"File not found: {file_path}")
        return False

    file_size_bytes = path.stat().st_size
    # Convert to appropriate unit
    if file_size_bytes < 1024:
        file_size_str = f"{file_size_bytes} bytes"
    elif file_size_bytes < 1024 * 1024:
        file_size_str = f"{file_size_bytes / 1024:.2f} KB"
    else:
        file_size_str = f"{file_size_bytes / (1024 * 1024):.2f} MB"

    # Get file extension and creation/modification times
    file_ext = path.suffix
    created_time = time.ctime(path.stat().st_ctime)
    modified_time = time.ctime(path.stat().st_mtime)

    # Check if file type is supported
    file_type_status = "Supported" if file_ext.lower() in SUPPORTED_TEXT_EXTENSIONS else "Unsupported"

    # Display file information
    logger.info("\nFile Information:")
    logger.info(f"  Path: {path.absolute()}")
    logger.info(f"  Size: {file_size_str}")
    logger.info(f"  Type: {file_ext} ({file_type_status})")
    logger.info(f"  Created: {created_time}")
    logger.info(f"  Modified: {modified_time}")

    # Try to determine the number of lines if it's a text file
    try:
        with open(path, 'r', encoding='utf-8') as f:
            line_count = sum(1 for _ in f)
        logger.info(f"  Lines: {line_count}")

        # Log additional details in debug mode
        logger.debug(f"  Average line length: {file_size_bytes / max(1, line_count):.2f} bytes")

    except UnicodeDecodeError:
        logger.warning("  Lines: Not a text file or contains non-UTF-8 characters")
    except Exception as e:
        logger.warning(f"  Lines: Unable to count (Error: {e})")

    return True

async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Ingest a file into LightRAG")
    parser.add_argument("file_path", help="Path to the file to ingest")
    parser.add_argument("--dry-run", action="store_true", help="Show file information without ingesting")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    parser.add_argument("--model", "-m", choices=list(AVAILABLE_MODELS.keys()), default="gpt-4o-mini",
                        help="Select the OpenAI model to use for ingestion")
    args = parser.parse_args()

    # Configure logging based on verbosity
    configure_logging(args.verbose)

    logger.info(f"Starting LightRAG file ingestion tool")
    logger.debug(f"Arguments: {args}")

    # Display file information
    if not display_file_info(args.file_path):
        logger.error(f"Invalid file: {args.file_path}")
        sys.exit(1)

    # If dry run, exit after displaying file information
    if args.dry_run:
        logger.info("Dry run completed. No ingestion performed.")
        return

    try:
        # Create and use the file ingestor
        logger.info(f"Starting ingestion process with model {args.model}...")
        ingestor = FileIngestor(
            file_path=args.file_path,
            model_name=args.model,
            verbose=args.verbose
        )
        await ingestor.ingest_content()
        await ingestor.finalize()
        logger.info("Ingestion completed successfully!")
    except Exception as e:
        logger.error(f"Error during ingestion: {e}")
        if args.verbose:
            import traceback
            logger.debug(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
