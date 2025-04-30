#!/usr/bin/env python3
import argparse
import os
import sys
import time
from datetime import datetime
from tqdm import tqdm

import os
from lightrag import LightRAG, QueryParam
# from lightrag.llm.openai import gpt_4o_mini_complete, gpt_4o_complete, openai_embed

from lightrag.llm.ollama import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc

def list_makdown_files(folder_path):
    """
    List all Markdown files in the specified folder.
    
    Args:
        folder_path: Path to the folder containing Markdown files
        
    Returns:
        list: A list of Markdown filenames
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist")
        sys.exit(1)
        
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a directory")
        sys.exit(1)
    
    markdown_files = []
    
    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith('.md'):
            print(filename)
            markdown_files.append(filename)
    
    if not markdown_files:
        print(f"No Markdown files found in '{folder_path}'")
    
    return markdown_files


def main():
    """Parse command line arguments and list Markdown files."""
    parser = argparse.ArgumentParser(
        description="List Markdown filenames in a specified directory"
    )
    parser.add_argument(
        "folder_path",
        help="Path to the folder containing Markdown files"
    )
    
    args = parser.parse_args()
    markdown_files = list_makdown_files(args.folder_path)

    # rag = LightRAG(
    #     working_dir=os.getcwd(),  # Use current working directory
    #     embedding_func=openai_embed,
    #     llm_model_func=gpt_4o_mini_complete
    # )

    # Initialize LightRAG with Ollama model
    rag = LightRAG(
        working_dir=os.getcwd(),
        llm_model_func=ollama_model_complete,  # Use Ollama model for text generation
        llm_model_name='qwen2m', # Your model name
        llm_model_kwargs={"options": {"num_ctx": 32768}},
        # Use Ollama embedding function
        embedding_func=EmbeddingFunc(
            embedding_dim=768,
            max_token_size=8192,
            func=lambda texts: ollama_embedding(
                texts,
                embed_model="nomic-embed-text"
            )
        ),
    )

    # Insert contents of each Markdown file
    successful_inserts = 0
    failed_inserts = 0
    total_files = len(markdown_files)

    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting to process {total_files} files...")
    start_time = time.time()
    
    for filename in tqdm(markdown_files, desc="Processing files", unit="file", ncols=100):
        full_path = os.path.join(args.folder_path, filename)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                tqdm.write(f"[{datetime.now().strftime('%H:%M:%S')}] Processing: {filename}")
                rag.insert(content)
                successful_inserts += 1
        except Exception as e:
            tqdm.write(f"\n[{datetime.now().strftime('%H:%M:%S')}] Error processing {filename}: {e}")
            failed_inserts += 1
            continue

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Processing complete:")
    print(f"✓ Successfully processed: {successful_inserts} files")
    if failed_inserts > 0:
        print(f"✗ Failed to process: {failed_inserts} files")
    print(f"Total insertion time: {elapsed_time:.2f} seconds")

    # Perform queries with timing
    # modes = ["naive", "local", "global", "hybrid", "mix"]

    # Perform naive search
    mode="naive"
    # Perform local search
    mode="local"
    # Perform global search
    mode="global"
    # Perform hybrid search
    mode="hybrid"
    # Mix mode Integrates knowledge graph and vector retrieval.
    mode="mix"

    query = "What are the biggest tax benefits to businesses?"
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running {mode} query...")
    query_start = time.time()
    result = rag.query(query, param=QueryParam(mode=mode))
    query_end = time.time()
    query_time = query_end - query_start
    print(f"Query time ({mode} mode): {query_time:.2f} seconds")
    print(f"Result: {result}\n")
    
    # print("\nPerforming queries in different modes:")
    # for mode in modes:
    #     print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running {mode} query...")
    #     query_start = time.time()
    #     result = rag.query(query, param=QueryParam(mode=mode))
    #     query_end = time.time()
    #     query_time = query_end - query_start
    #     print(f"Query time ({mode} mode): {query_time:.2f} seconds")
    #     print(f"Result: {result}\n")


if __name__ == "__main__":
    main()
