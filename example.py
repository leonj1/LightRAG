import os
from dotenv import load_dotenv

load_dotenv()

# Disable CUDA for transformers to avoid compilation issues
os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from typing import Iterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document as LCDocument

from docling.document_converter import DocumentConverter

class DoclingPDFLoader(BaseLoader):
    def __init__(self, file_path: str | list[str]) -> None:
        self.file_path = file_path if isinstance(file_path, list) else [file_path]
        self._converter = DocumentConverter()

    def lazy_load(self) -> Iterator[LCDocument]:
        for source in self.file_path:
            dl_doc = self._converter.convert(source).document
            text = dl_doc.export_to_markdown()
            yield LCDocument(page_content=text)

FILE_PATH = "https://raw.githubusercontent.com/DS4SD/docling/main/tests/data/pdf/2206.01062.pdf"

from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = DoclingPDFLoader(file_path=FILE_PATH)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
docs = loader.load()
splits = text_splitter.split_documents(docs)

# Print information about the loaded and split documents
print(f"Number of documents loaded: {len(docs)}")
print(f"Number of splits created: {len(splits)}")
if splits:
    print(f"First split content (preview): {splits[0].page_content[:200]}...")
