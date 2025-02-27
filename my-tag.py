#!/usr/bin/env python3
import argparse
import os
import sys

import os
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, gpt_4o_complete, openai_embed

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

    rag = LightRAG(
        working_dir=os.getcwd(),  # Use current working directory
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete
    )

    # Insert contents of each Markdown file
    from tqdm import tqdm
    for filename in tqdm(markdown_files, desc="Processing files"):
        full_path = os.path.join(args.folder_path, filename)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                rag.insert(content)
        except Exception as e:
            print(f"\nError processing {filename}: {e}")

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

    rag.query(
        "What are the biggest tax benefits to businesses?",
        param=QueryParam(mode=mode)
    )    

    # The function now returns the list of files, which can be used for further processing
    # For example, you could count them:
    if markdown_files:
        print(f"\nTotal Markdown files found: {len(markdown_files)}")


if __name__ == "__main__":
    main()
