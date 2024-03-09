from fastapi import UploadFile, Response
from fastapi.responses import StreamingResponse
from moviepy.editor import VideoFileClip, AudioFileClip
from app.subtitles import extract_and_translate_subtitles
from app.audio import translate_text_to_audio
import io
from pathlib import Path

def process_video_upload(file: UploadFile) -> bytes:
    # Save the uploaded video file
    with open("uploaded_video.mp4", "wb") as f:
        f.write(file.file.read())

    # Extract audio from uploaded video
    video = VideoFileClip("uploaded_video.mp4")
    audio = video.audio
    audio.write_audiofile("uploaded_audio.wav")

    # Extract and translate subtitles
    translated_subtitles = extract_and_translate_subtitles("uploaded_audio.wav")

    # Convert translated subtitles to Hindi audio
    hindi_audio = translate_text_to_audio(translated_subtitles)
    with open("translated_audio.wav", "wb") as f:
        f.write(hindi_audio)

    # Merge translated audio with original video
    translated_audio = AudioFileClip("translated_audio.wav")
    video = video.set_audio(translated_audio)

    # Write the video to a file on disk
    output_filename = "translated_video.mp4"
    video.write_videofile(output_filename, codec="libx264")

    # Read the contents of the file into a BytesIO object
    video_bytes = Path(output_filename).read_bytes()

    return video_bytes



