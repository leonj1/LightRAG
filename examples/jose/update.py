#!/usr/bin/env python3
import os
import sys
import argparse
import asyncio
import logging
import difflib
from pathlib import Path

from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, gpt_4o_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger, compute_mdhash_id

# Define working directory for LightRAG (same as in ingest.py and query.py)
WORKING_DIR = "./jose_rag_storage"

# Available models
AVAILABLE_MODELS = {
    "gpt-4o-mini": gpt_4o_mini_complete,
    "gpt-4o": gpt_4o_complete,
}

# Configure logging
logger = logging.getLogger("update")

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

class DocumentUpdater:
    def __init__(self, original_file, modified_file, model_name="gpt-4o-mini", verbose=False):
        """Initialize the document updater with original and modified files."""
        self.original_file = Path(original_file) if original_file else None
        self.modified_file = Path(modified_file)
        self.model_name = model_name
        self.verbose = verbose
        
        # Validate model name
        if self.model_name not in AVAILABLE_MODELS:
            raise ValueError(f"Invalid model name: {self.model_name}. Available models: {', '.join(AVAILABLE_MODELS.keys())}")
        
        self.model_func = AVAILABLE_MODELS[self.model_name]
        
        # Check if working directory exists
        if not os.path.exists(WORKING_DIR):
            raise FileNotFoundError(f"Working directory not found: {WORKING_DIR}. Please run ingest.py first.")
        
        # Check if modified file exists
        if not self.modified_file.exists():
            raise FileNotFoundError(f"Modified file not found: {self.modified_file}")
        
        # Check if original file exists (if provided)
        if self.original_file and not self.original_file.exists():
            raise FileNotFoundError(f"Original file not found: {self.original_file}")
        
        self.rag = None
        self.original_content = None
        self.modified_content = None
        self.original_doc_id = None
        
        logger.debug(f"DocumentUpdater initialized with model {self.model_name}")
    
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
    
    def read_file_content(self, file_path):
        """Read the content of a file."""
        logger.info(f"Reading file: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            content_length = len(content)
            logger.debug(f"Read {content_length} characters from file")
            
            return content
            
        except UnicodeDecodeError:
            logger.error(f"Failed to read file as UTF-8 text: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error reading file: {e}")
            raise
    
    async def find_original_document_id(self):
        """Find the document ID of the original file in the database."""
        if not self.rag:
            await self.initialize_rag()
        
        if not self.original_file:
            logger.info("No original file provided, will search by content")
            return None
        
        # Read original content
        self.original_content = self.read_file_content(self.original_file)
        
        # Compute document ID based on content
        self.original_doc_id = compute_mdhash_id(self.original_content, prefix="doc-")
        
        # Check if document exists in database
        doc_exists = await self.rag.full_docs.get_by_id(self.original_doc_id)
        
        if doc_exists:
            logger.info(f"Found original document with ID: {self.original_doc_id}")
            return self.original_doc_id
        else:
            logger.warning(f"Original document not found in database")
            return None
    
    async def find_document_by_path(self, file_path):
        """Find document IDs by file path."""
        if not self.rag:
            await self.initialize_rag()
        
        # Get all documents
        all_docs = await self.rag.doc_status.get_all()
        
        # Find documents with matching file path
        matching_docs = []
        for doc_id, doc_data in all_docs.items():
            if isinstance(doc_data, dict) and doc_data.get("file_path") == str(file_path):
                matching_docs.append(doc_id)
        
        if matching_docs:
            logger.info(f"Found {len(matching_docs)} documents with file path: {file_path}")
            return matching_docs
        else:
            logger.warning(f"No documents found with file path: {file_path}")
            return []
    
    def compare_documents(self):
        """Compare original and modified documents to identify changes."""
        # Read modified content
        self.modified_content = self.read_file_content(self.modified_file)
        
        # If original content is not available, we can't compare
        if not self.original_content:
            logger.warning("Original content not available for comparison")
            return None
        
        # Compare documents
        diff = difflib.unified_diff(
            self.original_content.splitlines(),
            self.modified_content.splitlines(),
            lineterm='',
            n=3  # Context lines
        )
        
        # Convert diff to string
        diff_text = '\n'.join(diff)
        
        # Calculate change percentage
        total_lines = len(self.original_content.splitlines())
        changed_lines = sum(1 for line in diff_text.splitlines() if line.startswith('+') or line.startswith('-'))
        change_percentage = (changed_lines / (total_lines * 2)) * 100 if total_lines > 0 else 0
        
        logger.info(f"Documents differ by approximately {change_percentage:.2f}% of lines")
        
        if self.verbose:
            logger.debug(f"Diff:\n{diff_text}")
        
        return {
            "diff": diff_text,
            "change_percentage": change_percentage,
            "total_lines": total_lines,
            "changed_lines": changed_lines
        }
    
    async def delete_document(self, doc_id):
        """Delete a document from the database."""
        if not self.rag:
            await self.initialize_rag()
        
        logger.info(f"Deleting document with ID: {doc_id}")
        
        try:
            await self.rag.adelete_by_doc_id(doc_id)
            logger.info(f"Successfully deleted document: {doc_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting document: {e}")
            return False
    
    async def ingest_document(self, file_path):
        """Ingest a document into the database."""
        if not self.rag:
            await self.initialize_rag()
        
        logger.info(f"Ingesting document: {file_path}")
        
        try:
            # Read content if not already read
            if file_path == self.modified_file and self.modified_content:
                content = self.modified_content
            else:
                content = self.read_file_content(file_path)
            
            # Ingest document
            await self.rag.ainsert(
                content,
                file_paths=str(file_path)
            )
            
            logger.info(f"Successfully ingested document: {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error ingesting document: {e}")
            return False
    
    async def update_document(self, strategy="replace", threshold=10.0):
        """Update a document in the database.
        
        Strategies:
        - replace: Delete the old document and ingest the new one (default)
        - add: Keep the old document and add the new one
        - auto: Choose strategy based on change percentage threshold
        """
        if not self.rag:
            await self.initialize_rag()
        
        # Find original document ID
        original_doc_id = await self.find_original_document_id()
        
        # If original document ID not found by content, try finding by path
        if not original_doc_id and self.original_file:
            matching_docs = await self.find_document_by_path(self.original_file)
            if matching_docs:
                original_doc_id = matching_docs[0]
        
        # Compare documents if both are available
        comparison = None
        if self.original_content and self.modified_file:
            comparison = self.compare_documents()
        
        # Determine strategy
        actual_strategy = strategy
        if strategy == "auto" and comparison:
            if comparison["change_percentage"] <= threshold:
                actual_strategy = "replace"
                logger.info(f"Auto strategy: Using 'replace' (change percentage: {comparison['change_percentage']:.2f}%)")
            else:
                actual_strategy = "add"
                logger.info(f"Auto strategy: Using 'add' (change percentage: {comparison['change_percentage']:.2f}%)")
        
        # Execute strategy
        if actual_strategy == "replace" and original_doc_id:
            # Delete original document
            delete_success = await self.delete_document(original_doc_id)
            if not delete_success:
                logger.warning("Failed to delete original document, proceeding with ingestion anyway")
            
            # Ingest modified document
            ingest_success = await self.ingest_document(self.modified_file)
            return ingest_success
        
        elif actual_strategy == "add" or not original_doc_id:
            # Just ingest the modified document
            ingest_success = await self.ingest_document(self.modified_file)
            return ingest_success
        
        else:
            logger.error(f"Unknown strategy: {actual_strategy}")
            return False
    
    async def finalize(self):
        """Finalize the LightRAG instance."""
        if self.rag:
            logger.debug("Finalizing LightRAG storages...")
            await self.rag.finalize_storages()
            logger.info("LightRAG instance finalized")

async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Update a document in LightRAG database")
    parser.add_argument("modified_file", help="Path to the modified file")
    parser.add_argument("--original", "-o", help="Path to the original file (if not provided, will try to find by content)")
    parser.add_argument("--strategy", "-s", choices=["replace", "add", "auto"], default="auto",
                        help="Update strategy: replace, add, or auto (default: auto)")
    parser.add_argument("--threshold", "-t", type=float, default=10.0,
                        help="Change percentage threshold for auto strategy (default: 10.0)")
    parser.add_argument("--model", "-m", choices=list(AVAILABLE_MODELS.keys()), default="gpt-4o-mini",
                        help="Select the OpenAI model to use (default: gpt-4o-mini)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()
    
    # Configure logging based on verbosity
    configure_logging(args.verbose)
    
    logger.info(f"Starting LightRAG document update tool")
    logger.debug(f"Arguments: {args}")
    
    try:
        # Check if working directory exists
        if not os.path.exists(WORKING_DIR):
            print(f"\nError: Working directory '{WORKING_DIR}' not found.")
            print("You need to run the ingest.py script first to create and populate the database.")
            print("\nExample:")
            print("  python examples/jose/ingest.py examples/jose/sample.txt")
            sys.exit(1)
        
        # Create updater
        updater = DocumentUpdater(
            original_file=args.original,
            modified_file=args.modified_file,
            model_name=args.model,
            verbose=args.verbose
        )
        
        # Update document
        success = await updater.update_document(
            strategy=args.strategy,
            threshold=args.threshold
        )
        
        # Finalize
        await updater.finalize()
        
        if success:
            logger.info("Document update completed successfully!")
        else:
            logger.error("Document update failed")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Error: {e}")
        if args.verbose:
            import traceback
            logger.debug(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
