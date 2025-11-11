import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_PATH = "your model path"
EMBEDDING_MODEL = "your embedding model"
CHROMA_DB_DIR = "vector_db"
UPLOAD_DIR = "uploaded_pdfs"

