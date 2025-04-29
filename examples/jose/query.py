#!/usr/bin/env python3
import os
import sys
import argparse
import asyncio
import inspect
import logging

from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, gpt_4o_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger

# Define working directory for LightRAG (same as in ingest.py)
WORKING_DIR = "./jose_rag_storage"

# Available models
AVAILABLE_MODELS = {
    "gpt-4o-mini": gpt_4o_mini_complete,
    "gpt-4o": gpt_4o_complete,
}

# Available query modes
AVAILABLE_MODES = ["naive", "local", "global", "hybrid", "mix"]

# Configure logging
logger = logging.getLogger("query")

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

class LightRAGQuerier:
    def __init__(self, model_name="gpt-4o-mini", verbose=False):
        """Initialize the LightRAG querier."""
        self.model_name = model_name
        self.verbose = verbose

        # Validate model name
        if self.model_name not in AVAILABLE_MODELS:
            raise ValueError(f"Invalid model name: {self.model_name}. Available models: {', '.join(AVAILABLE_MODELS.keys())}")

        self.model_func = AVAILABLE_MODELS[self.model_name]

        self.rag = None
        # Initialize conversation history
        self.conversation_history = []
        logger.debug(f"LightRAGQuerier initialized with model {self.model_name}")

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

    async def query(self, query_text, mode="hybrid", stream=False, use_history=True, history_turns=3):
        """Query the LightRAG instance."""
        if not self.rag:
            await self.initialize_rag()

        logger.info(f"Querying with mode: {mode}")
        logger.debug(f"Query text: {query_text}")

        # Create query parameters
        param = QueryParam(mode=mode, stream=stream)

        # Add conversation history if enabled
        if use_history and self.conversation_history:
            logger.debug(f"Using conversation history with {len(self.conversation_history)} messages")
            param.conversation_history = self.conversation_history
            param.history_turns = history_turns

        # Perform the query
        try:
            logger.debug("Executing query...")
            response = await self.rag.aquery(query_text, param=param)

            # Add to conversation history
            self.conversation_history.append({"role": "user", "content": query_text})

            # For streaming responses, we need to collect the full response to add to history
            if stream and inspect.isasyncgen(response):
                logger.debug("Handling streaming response...")
                # Create a wrapper that collects the full response while yielding chunks
                full_response = ""

                async def collect_and_yield():
                    nonlocal full_response
                    async for chunk in response:
                        full_response += chunk
                        yield chunk
                    # Add to conversation history after collecting all chunks
                    self.conversation_history.append({"role": "assistant", "content": full_response})

                return collect_and_yield()
            else:
                # For non-streaming responses, add directly to history
                self.conversation_history.append({"role": "assistant", "content": response})

            logger.debug("Query completed successfully")
            return response

        except Exception as e:
            logger.error(f"Error during query: {e}")
            raise

    async def get_database_info(self):
        """Get information about the LightRAG database."""
        if not self.rag:
            await self.initialize_rag()

        try:
            # Get information about the database
            info = {
                "working_directory": WORKING_DIR,
                "model": self.model_name,
                "conversation_history_length": len(self.conversation_history) // 2,  # Pairs of messages
            }

            # Try to get more detailed information from the storages
            if hasattr(self.rag, "text_chunks") and self.rag.text_chunks:
                # Count documents
                try:
                    all_keys = await self.rag.text_chunks.get_all_keys()
                    info["document_count"] = len(all_keys)
                except:
                    info["document_count"] = "Unknown"

            return info
        except Exception as e:
            logger.error(f"Error getting database info: {e}")
            return {"error": str(e)}

    def clear_history(self):
        """Clear the conversation history."""
        logger.info("Clearing conversation history")
        self.conversation_history = []

    async def finalize(self):
        """Finalize the LightRAG instance."""
        if self.rag:
            logger.debug("Finalizing LightRAG storages...")
            await self.rag.finalize_storages()
            logger.info("LightRAG instance finalized")

async def print_stream(stream):
    """Print streaming response chunks."""
    async for chunk in stream:
        print(chunk, end="", flush=True)
    print()  # Add a newline at the end

async def save_response_to_file(response, filename):
    """Save response to a file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response)
        print(f"Response saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving response to file: {e}")
        return False

async def interactive_mode(querier, mode, stream, use_history=True):
    """Run in interactive mode, allowing multiple queries."""
    print("\n=== LightRAG Interactive Query Mode ===")
    print(f"Using model: {querier.model_name}")
    print(f"Query mode: {mode}")
    print(f"Streaming: {'enabled' if stream else 'disabled'}")
    print(f"Conversation history: {'enabled' if use_history else 'disabled'}")
    print("\nSpecial commands:")
    print("  /help - Show this help message")
    print("  /exit, /quit - Exit the program")
    print("  /info - Show database information")
    print("  /clear - Clear conversation history")
    print("  /save <filename> - Save last response to file")
    print("  /mode <mode> - Change query mode (naive, local, global, hybrid, mix)")
    print("  /stream <on|off> - Enable or disable streaming")
    print("  /history <on|off> - Enable or disable conversation history")
    print("=======================================\n")

    # Initialize variables
    current_mode = mode
    current_stream = stream
    current_use_history = use_history
    last_response = None

    try:
        # Get database info
        db_info = await querier.get_database_info()
        print("Database information:")
        for key, value in db_info.items():
            print(f"  {key}: {value}")

        while True:
            # Get query from user
            query_text = input("\nEnter your query (or /help for commands): ")

            # Process special commands
            if query_text.startswith('/'):
                cmd_parts = query_text.split(maxsplit=1)
                cmd = cmd_parts[0].lower()

                if cmd in ['/exit', '/quit']:
                    print("Exiting interactive mode...")
                    break

                elif cmd == '/help':
                    print("\nSpecial commands:")
                    print("  /help - Show this help message")
                    print("  /exit, /quit - Exit the program")
                    print("  /info - Show database information")
                    print("  /clear - Clear conversation history")
                    print("  /save <filename> - Save last response to file")
                    print("  /mode <mode> - Change query mode (naive, local, global, hybrid, mix)")
                    print("  /stream <on|off> - Enable or disable streaming")
                    print("  /history <on|off> - Enable or disable conversation history")
                    continue

                elif cmd == '/info':
                    db_info = await querier.get_database_info()
                    print("\nDatabase information:")
                    for key, value in db_info.items():
                        print(f"  {key}: {value}")
                    continue

                elif cmd == '/clear':
                    querier.clear_history()
                    print("Conversation history cleared")
                    continue

                elif cmd == '/save':
                    if len(cmd_parts) < 2:
                        print("Please specify a filename: /save <filename>")
                    elif last_response is None:
                        print("No response to save yet")
                    else:
                        filename = cmd_parts[1]
                        await save_response_to_file(last_response, filename)
                    continue

                elif cmd == '/mode':
                    if len(cmd_parts) < 2 or cmd_parts[1] not in AVAILABLE_MODES:
                        print(f"Please specify a valid mode: {', '.join(AVAILABLE_MODES)}")
                    else:
                        current_mode = cmd_parts[1]
                        print(f"Query mode changed to: {current_mode}")
                    continue

                elif cmd == '/stream':
                    if len(cmd_parts) < 2 or cmd_parts[1].lower() not in ['on', 'off']:
                        print("Please specify 'on' or 'off'")
                    else:
                        current_stream = (cmd_parts[1].lower() == 'on')
                        print(f"Streaming {'enabled' if current_stream else 'disabled'}")
                    continue

                elif cmd == '/history':
                    if len(cmd_parts) < 2 or cmd_parts[1].lower() not in ['on', 'off']:
                        print("Please specify 'on' or 'off'")
                    else:
                        current_use_history = (cmd_parts[1].lower() == 'on')
                        print(f"Conversation history {'enabled' if current_use_history else 'disabled'}")
                    continue

                else:
                    print(f"Unknown command: {cmd}")
                    continue

            # Skip empty queries
            if not query_text.strip():
                continue

            # Execute query
            try:
                response = await querier.query(
                    query_text,
                    mode=current_mode,
                    stream=current_stream,
                    use_history=current_use_history
                )

                # Handle response
                print("\nResponse:")
                if current_stream and inspect.isasyncgen(response):
                    # For streaming responses, we need to collect the full response
                    full_response = ""
                    async for chunk in response:
                        print(chunk, end="", flush=True)
                        full_response += chunk
                    print()  # Add a newline at the end
                    last_response = full_response
                else:
                    print(response)
                    last_response = response

            except Exception as e:
                print(f"Error: {e}")

    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
    finally:
        await querier.finalize()

async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Query LightRAG database")
    parser.add_argument("--query", "-q", nargs='?', const='',
                        help="Query text (if provided without value or not provided at all, interactive mode will be used)")
    parser.add_argument("--mode", "-m", choices=AVAILABLE_MODES, default="hybrid",
                        help="Query mode to use (default: hybrid)")
    parser.add_argument("--model", choices=list(AVAILABLE_MODELS.keys()), default="gpt-4o-mini",
                        help="Select the OpenAI model to use for querying (default: gpt-4o-mini)")
    parser.add_argument("--stream", "-s", action="store_true", help="Enable streaming response")
    parser.add_argument("--no-history", action="store_true", help="Disable conversation history")
    parser.add_argument("--output", "-o", help="Save response to specified file")
    parser.add_argument("--info", "-i", action="store_true", help="Display database information and exit")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    # Configure logging based on verbosity
    configure_logging(args.verbose)

    logger.info(f"Starting LightRAG query tool")
    logger.debug(f"Arguments: {args}")

    try:
        # Check if working directory exists before creating querier
        if not os.path.exists(WORKING_DIR):
            print(f"\nError: Working directory '{WORKING_DIR}' not found.")
            print("You need to run the ingest.py script first to create and populate the database.")
            print("\nExample:")
            print("  python examples/jose/ingest.py examples/jose/sample.txt")
            sys.exit(1)

        # Create querier
        querier = LightRAGQuerier(model_name=args.model, verbose=args.verbose)

        # If info flag is set, display database info and exit
        if args.info:
            # Initialize RAG to get info
            await querier.initialize_rag()
            db_info = await querier.get_database_info()
            print("\nDatabase Information:")
            for key, value in db_info.items():
                print(f"  {key}: {value}")
            await querier.finalize()
            return

        # Check if query is provided with a non-empty value
        if args.query is not None and args.query.strip():
            # Single query mode
            response = await querier.query(
                args.query,
                mode=args.mode,
                stream=args.stream,
                use_history=not args.no_history
            )

            # Handle response
            print("\nResponse:")
            if args.stream and inspect.isasyncgen(response):
                # For streaming responses, we need to collect the full response if saving to file
                if args.output:
                    full_response = ""
                    async for chunk in response:
                        print(chunk, end="", flush=True)
                        full_response += chunk
                    print()  # Add a newline at the end

                    # Save to file if requested
                    if args.output:
                        await save_response_to_file(full_response, args.output)
                else:
                    await print_stream(response)
            else:
                print(response)

                # Save to file if requested
                if args.output:
                    await save_response_to_file(response, args.output)

            # Finalize
            await querier.finalize()
        else:
            # Interactive mode - used when:
            # 1. No --query argument is provided
            # 2. --query is provided without a value
            # 3. --query is provided with an empty value
            await interactive_mode(querier, args.mode, args.stream, not args.no_history)

    except Exception as e:
        logger.error(f"Error: {e}")
        if args.verbose:
            import traceback
            logger.debug(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
