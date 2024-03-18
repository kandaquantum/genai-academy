from pathlib import Path
from openai import OpenAI

client = OpenAI()

def generate_speech(text, voice="alloy", model="tts-1"):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text
    )

    response.stream_to_file(speech_file_path)
    return speech_file