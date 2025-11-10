from fastapi import FastAPI
from app.routes import upload_routes, qa_routes

app = FastAPI(title="PDF Knowledge Assistant")

app.include_router(upload_routes.router, prefix="/api", tags=["Upload"])
app.include_router(qa_routes.router, prefix="/api", tags=["Q&A"])

@app.get("/")
def root():
    return {"message": "PDF Assistant API is running"}
