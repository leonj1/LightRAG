import os
import asyncio
import argparse
import logging
import logging.config
import time
import datetime
from tabulate import tabulate
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import logger, set_verbose_debug

WORKING_DIR = "./dickens"


def configure_logging():
    """Configure logging for the application"""

    # Reset any existing handlers to ensure clean configuration
    for logger_name in ["uvicorn", "uvicorn.access", "uvicorn.error", "lightrag"]:
        logger_instance = logging.getLogger(logger_name)
        logger_instance.handlers = []
        logger_instance.filters = []

    # Get log directory path from environment variable or use current directory
    log_dir = os.getenv("LOG_DIR", os.getcwd())
    log_file_path = os.path.abspath(os.path.join(log_dir, "lightrag_demo_query_only.log"))

    print(f"\nLightRAG demo log file: {log_file_path}\n")
    os.makedirs(os.path.dirname(log_dir), exist_ok=True)

    # Get log file max size and backup count from environment variables
    log_max_bytes = int(os.getenv("LOG_MAX_BYTES", 10485760))  # Default 10MB
    log_backup_count = int(os.getenv("LOG_BACKUP_COUNT", 5))  # Default 5 backups

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(levelname)s: %(message)s",
                },
                "detailed": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                },
            },
            "handlers": {
                "console": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stderr",
                },
                "file": {
                    "formatter": "detailed",
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": log_file_path,
                    "maxBytes": log_max_bytes,
                    "backupCount": log_backup_count,
                    "encoding": "utf-8",
                },
            },
            "loggers": {
                "lightrag": {
                    "handlers": ["console", "file"],
                    "level": "INFO",
                    "propagate": False,
                },
            },
        }
    )

    # Set the logger level to INFO
    logger.setLevel(logging.INFO)
    # Enable verbose debug if needed
    set_verbose_debug(os.getenv("VERBOSE_DEBUG", "false").lower() == "true")


if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)


async def initialize_rag():
    rag = LightRAG(
        working_dir=WORKING_DIR,
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
    )

    await rag.initialize_storages()
    await initialize_pipeline_status()

    return rag


async def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Run LightRAG queries with different modes')
    parser.add_argument('-q', '--query', required=True, help='The query to run against the RAG system')
    args = parser.parse_args()
    
    # Get the user query from command line arguments
    user_query = args.query
    
    # Check if OPENAI_API_KEY environment variable exists
    if not os.getenv("OPENAI_API_KEY"):
        print(
            "Error: OPENAI_API_KEY environment variable is not set. Please set this variable before running the program."
        )
        print("You can set the environment variable by running:")
        print("  export OPENAI_API_KEY='your-openai-api-key'")
        return  # Exit the async function

    # Dictionary to store timing information
    timing_info = {}
    
    try:
        # # Clear old data files
        # files_to_delete = [
        #     "graph_chunk_entity_relation.graphml",
        #     "kv_store_doc_status.json",
        #     "kv_store_full_docs.json",
        #     "kv_store_text_chunks.json",
        #     "vdb_chunks.json",
        #     "vdb_entities.json",
        #     "vdb_relationships.json",
        # ]

        # for file in files_to_delete:
        #     file_path = os.path.join(WORKING_DIR, file)
        #     if os.path.exists(file_path):
        #         os.remove(file_path)
        #         print(f"Deleting old file:: {file_path}")

        # Initialize RAG instance
        rag = await initialize_rag()

        # # Test embedding function
        # test_text = ["This is a test string for embedding."]
        # embedding = await rag.embedding_func(test_text)
        # embedding_dim = embedding.shape[1]
        # print("\n=======================")
        # print("Test embedding function")
        # print("========================")
        # print(f"Test dict: {test_text}")
        # print(f"Detected embedding dimension: {embedding_dim}\n\n")

        # with open("./book.txt", "r", encoding="utf-8") as f:
        #     await rag.ainsert(f.read())

        # Perform naive search
        print("\n=====================")
        print("Query mode: naive")
        print("=====================")
        start_time = time.time()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        logger.info(f"[{timestamp}] Starting naive query...")
        
        result = await rag.aquery(
            user_query, param=QueryParam(mode="naive")
        )
        
        end_time = time.time()
        duration = end_time - start_time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        logger.info(f"[{timestamp}] Completed naive query in {duration:.4f} seconds")
        timing_info["naive"] = {
            "start": start_time,
            "end": end_time,
            "duration": duration
        }
        print(result)

        # Perform local search
        print("\n=====================")
        print("Query mode: local")
        print("=====================")
        start_time = time.time()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        logger.info(f"[{timestamp}] Starting local query...")
        
        result = await rag.aquery(
            user_query, param=QueryParam(mode="local")
        )
        
        end_time = time.time()
        duration = end_time - start_time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        logger.info(f"[{timestamp}] Completed local query in {duration:.4f} seconds")
        timing_info["local"] = {
            "start": start_time,
            "end": end_time,
            "duration": duration
        }
        print(result)

        # Perform global search
        print("\n=====================")
        print("Query mode: global")
        print("=====================")
        start_time = time.time()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        logger.info(f"[{timestamp}] Starting global query...")
        
        result = await rag.aquery(
            user_query,
            param=QueryParam(mode="global"),
        )
        
        end_time = time.time()
        duration = end_time - start_time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        logger.info(f"[{timestamp}] Completed global query in {duration:.4f} seconds")
        timing_info["global"] = {
            "start": start_time,
            "end": end_time,
            "duration": duration
        }
        print(result)

        # Perform hybrid search
        print("\n=====================")
        print("Query mode: hybrid")
        print("=====================")
        start_time = time.time()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        logger.info(f"[{timestamp}] Starting hybrid query...")
        
        result = await rag.aquery(
            user_query,
            param=QueryParam(mode="hybrid"),
        )
        
        end_time = time.time()
        duration = end_time - start_time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        logger.info(f"[{timestamp}] Completed hybrid query in {duration:.4f} seconds")
        timing_info["hybrid"] = {
            "start": start_time,
            "end": end_time,
            "duration": duration
        }
        print(result)
        
        # Display timing summary table
        print("\n=====================")
        print("Query Timing Summary")
        print("=====================")
        
        # Prepare table data
        table_data = []
        for mode, times in timing_info.items():
            start_datetime = datetime.datetime.fromtimestamp(times["start"]).strftime("%H:%M:%S.%f")[:-3]
            end_datetime = datetime.datetime.fromtimestamp(times["end"]).strftime("%H:%M:%S.%f")[:-3]
            table_data.append([
                mode.capitalize(),
                start_datetime,
                end_datetime,
                f"{times['duration']:.4f}s"
            ])
        
        # Print the table
        headers = ["Query Mode", "Start Time", "End Time", "Duration"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if rag:
            await rag.finalize_storages()


if __name__ == "__main__":
    # Configure logging before running the main function
    configure_logging()
    asyncio.run(main())
    print("\nDone!")
