import os
import argparse
import glob
from pathlib import Path
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

# Disable CUDA for transformers to avoid compilation issues
os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from typing import Iterator, List

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document as LCDocument

from docling.document_converter import DocumentConverter

class DoclingPDFLoader(BaseLoader):
    def __init__(self, file_path: str | list[str]) -> None:
        self.file_path = file_path if isinstance(file_path, list) else [file_path]
        self._converter = DocumentConverter()

    def lazy_load(self) -> Iterator[LCDocument]:
        for source in self.file_path:
            try:
                dl_doc = self._converter.convert(source).document
                text = dl_doc.export_to_markdown()
                yield LCDocument(page_content=text, metadata={"source": source})
            except Exception as e:
                print(f"Error processing {source}: {str(e)}")

def process_pdf_files(input_folder: str, output_folder: str) -> None:
    """
    Process all PDF files in the input folder and save their markdown content to the output folder.
    
    Args:
        input_folder: Path to folder containing PDF files
        output_folder: Path to folder where markdown files will be saved
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Find all PDF files in the input folder
    pdf_files = glob.glob(os.path.join(input_folder, "**", "*.pdf"), recursive=True)
    
    if not pdf_files:
        print(f"No PDF files found in {input_folder}")
        return
    
    print(f"Found {len(pdf_files)} PDF files to process")
    
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    
    # Process each PDF file with a progress bar
    for pdf_file in tqdm(pdf_files, desc="Processing PDF files"):
        try:
            # Get relative path to maintain folder structure in output
            rel_path = os.path.relpath(pdf_file, input_folder)
            
            # Create output path with .md extension
            output_path = os.path.join(output_folder, os.path.splitext(rel_path)[0] + ".md")
            
            # Create parent directories if they don't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Load and process the PDF
            loader = DoclingPDFLoader(pdf_file)
            docs = loader.load()
            
            if not docs:
                print(f"No content extracted from {pdf_file}")
                continue
                
            splits = text_splitter.split_documents(docs)
            
            # Combine all splits and write to output file
            with open(output_path, "w", encoding="utf-8") as f:
                for split in splits:
                    f.write(split.page_content)
                    f.write("\n\n")
            
            print(f"Saved markdown content to {output_path}")
            
        except Exception as e:
            print(f"Error processing {pdf_file}: {str(e)}")

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Convert PDF files to markdown")
    parser.add_argument("input_folder", help="Folder containing PDF files to process")
    parser.add_argument("output_folder", help="Folder where markdown files will be saved")
    
    args = parser.parse_args()
    
    # Process the PDF files
    process_pdf_files(args.input_folder, args.output_folder)
    
    print("Processing complete!")

if __name__ == "__main__":
    main()
