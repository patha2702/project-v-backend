
from fastapi import FastAPI, UploadFile, File
from app.video import process_video_upload
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    video_bytes = process_video_upload(file)
    return StreamingResponse(io.BytesIO(video_bytes), media_type="video/mp4")