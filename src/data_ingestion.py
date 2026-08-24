import sys
import os
from dotenv import load_dotenv
from pathlib import Path
from typing import Any,List,Dictionary,Optional
project_root=Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0,str(project_root))
load_dotenv(dotenv_path=project_root/'.env')
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore,RetrievalMode 
from qdrant_client import QdrantClient,models
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from src.data_parsing import Complex_pdf_parser
logger = CustomLogger().get_logger(__name__)







class multimodal_ingestion:
    def __init__(self,document_path:str):
        pass
    def _validate_config(self):
        pass
    def _ensure_collection(self):
        pass
    def _document_id(self):
        pass
    def _point_id(self):
        pass
    def _chunking(self):
        pass
    def prepare_document(self):
        pass
    def _deleting_existing_doc(self):
        pass
    def _ingest_document(self):
        pass
    def get_vectorstore(self):
        pass