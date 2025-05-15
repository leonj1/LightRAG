import asyncio
import argparse
from lightrag.utils import logger
import os
import asyncio
import logging
import logging.config
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import logger, set_verbose_debug

WORKING_DIR = "./dickens"

async def initialize_rag():
    rag = LightRAG(
        working_dir=WORKING_DIR,
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
    )

    await rag.initialize_storages()
    await initialize_pipeline_status()

    return rag
# Simple response function that doesn't require any initialization
async def simple_query(query, mode="naive"):
    rag = await initialize_rag()
    return await rag.aquery(
        query,
        param=QueryParam(
            mode="naive",
            user_prompt="Do not include any references section in your response.",
        )
    )

async def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Run LightRAG queries with different modes')
    parser.add_argument('-q', '--query', required=True, help='The query to run against the RAG system')
    parser.add_argument('-m', '--mode', default="naive", choices=["naive", "local", "global", "hybrid"], 
                        help='Query mode to use (default: naive)')
    args = parser.parse_args()
    
    # Get the user query from command line arguments
    user_query = args.query
    query_mode = args.mode
    
    try:
        print(await simple_query(user_query, query_mode))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
