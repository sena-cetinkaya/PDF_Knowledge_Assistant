from fastapi import APIRouter, UploadFile, File
import os
from app.services.pdf_service import process_pdf
from app.utils.config import UPLOAD_DIR

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = process_pdf(file_path)
    return result
