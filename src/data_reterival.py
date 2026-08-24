import sys
import json
import os
from pathlib import Path
from dotenv import load_dotenv
project_root=Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0,str(project_root))
load_dotenv(dotenv_path=project_root/'.env')
from langchain_qdrant import QdrantVectorStore,RetrievalMode
from qdrant_client import QdrantClient,models
from langchain_huggingface import HuggingFaceEmbeddings
from typing import Any,List,Dictionary,Optional
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
logger = CustomLogger().get_logger(__name__)
class multmodal_reterival:
    def __init__(self):
        pass
    def _validate_config(self):
        pass
    def _validate_collection(self):
        pass
    def _normalize_content_type(self):
        pass
    def build_filter(self):
        pass
    def reterieve_with_score(self):
        pass
    def as_langchain_reterival(self):
        pass
    def format_result(self):
        pass
    def collection_status(self):
        pass