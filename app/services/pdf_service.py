import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from app.utils.config import *

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CHROMA_DB_DIR, exist_ok=True)

def process_pdf(file_path: str):
    # Upload PDF / PDF yükleme
    loader = PyPDFLoader(file_path)
    data = loader.load()

    # Breaking the text into parts / Metni parçalara ayırma
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
    text_chunks = text_splitter.split_documents(data)

    # Create embeddings / Embeddings oluştur
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL, model_kwargs={"device": device})

    # Create Chrome database / Chroma veritabanı oluştur
    vector_store = Chroma.from_documents(text_chunks, embeddings, persist_directory=CHROMA_DB_DIR)
    vector_store.persist()

    return {"message": "The PDF was successfully processed and saved to the database."}

