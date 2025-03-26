from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app import crud
from app.models import FileUpload
from app.utils import read_csv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file format")
    
    file_content = await file.read()
    file_path = f"temp/{file.filename}"
    
    with open(file_path, "wb") as f:
        f.write(file_content)

    document = read_csv(file_path)
    file_id = await crud.upload_file(FileUpload(file_id=file.filename, file_name=file.filename, document=document))
    
    return JSONResponse(content={"file_id": file_id, "message": "Upload successful"})

@app.get("/files")
async def list_files():
    files = await crud.get_files()
    return {"files": files}

@app.post("/query")
async def query_file(file_id: str, query: str):
    file = await crud.get_file(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    
    # Here you would implement the logic to query the CSV data using LLM
    response = f"Querying {file['file_name']} with query: {query}"
    return {"response": response}

@app.delete("/file/{file_id}")
async def delete_file(file_id: str):
    success = await crud.delete_file(file_id)
    if not success:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted successfully"}