import sys
import json
from pathlib import Path
from typing import Any,List,Dictionary,Optional
project_root=Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))
import pymupdf as fitz
import pytesseract
import pdfplumber
from PIL import Image
from langchain_core.documents import Document
from langchain_core.document_loaders import DocumentLoader
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
logger = CustomLogger().get_logger(__name__)





class Complex_pdf_parser:
    def __init__(self, pdf_path):
        pass
    def _validate_pdf(self):
        pass
    def _create_outputdir(self):
        pass
    def _config_tesscract(self):
        pass
    def run_ocr_on_image(self):
        pass
    def extract_text_images(self):
        pass
    def extract_table(self):
        pass
    def create_langchain_doc(self):
        pass
    def _saveoutput_json(self):
        pass
    def saveoutput(self):
        pass

