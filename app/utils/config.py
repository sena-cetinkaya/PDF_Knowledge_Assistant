import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_PATH = "C:/Users/LENOVO/PycharmProjects/pdf_assistant/mistral-7b-openorca.Q4_0.gguf"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHROMA_DB_DIR = "vector_db"
UPLOAD_DIR = "uploaded_pdfs"
