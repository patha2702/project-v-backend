# app/subtitles.py
import speech_recognition as sr
from googletrans import Translator

def extract_and_translate_subtitles(audio_path):
    # Extract subtitles from audio
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        subtitles = recognizer.recognize_google(audio_data)

    # Translate subtitles to Hindi
    translator = Translator()
    translated_subtitles = translator.translate(subtitles, src="en", dest="hi").text

    return translated_subtitles
