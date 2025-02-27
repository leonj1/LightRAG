#!/usr/bin/env python3
import argparse
import os
import sys

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
    
    # The function now returns the list of files, which can be used for further processing
    # For example, you could count them:
    if markdown_files:
        print(f"\nTotal Markdown files found: {len(markdown_files)}")


if __name__ == "__main__":
    main()