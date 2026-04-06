from fastapi import FastAPI , HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from downloader import download_mp3
from utils import get_filename

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
@app.get("/")
def home():
    return FileResponse(os.path.join(BASE_DIR,"docs.html"))

@app.get("/download")
def download(url:str):
    try:
        file_path=download_mp3(url)
        return FileResponse(file_path,media_type="audio/mpeg",filename=get_filename(file_path),headers={"Content-Disposition": f"attachment; filename={get_filename(file_path)}"}),
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))