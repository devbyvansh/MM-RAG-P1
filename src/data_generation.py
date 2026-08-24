import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
project_root=Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0,str(project_root))
load_dotenv(dotenv_path=project_root/'.env')

class rag_generator:
    def __init__(self):
        pass
    def _validate_config(self):
        pass
    def load_tokenizer(self):
        pass
    def image_to_url(self)->str:
        pass
    def _sourcelabel(self):
        pass
    def prepare_context(self):
        pass
    def _build_messages(self):
        pass
    def extract_response_text(self)->str:
        pass
    def _usemetadata(self):
        pass
    def generate(self):
        pass
    def answer_question(self):
        pass
    
