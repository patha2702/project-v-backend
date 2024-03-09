
from gtts import gTTS
import io

def translate_text_to_audio(text, language='hi'):
    tts = gTTS(text=text, lang=language)
    audio_bytes_io = io.BytesIO()
    tts.write_to_fp(audio_bytes_io)
    audio_bytes_io.seek(0)
    return audio_bytes_io.getvalue()
