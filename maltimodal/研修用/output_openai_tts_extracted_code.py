from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
from pathlib import Path
from openai import OpenAI
client = OpenAI()

voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

for voice in voices:
    speech_file_path = Path(__file__).parent / f"{voice}.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input="This is a test of the different voices available in the OpenAI Audio API."
    )
    response.stream_to_file(speech_file_path)
from pathlib import Path
from openai import OpenAI
client = OpenAI()

texts = {
    "en": "This is a test of the multilingual capabilities of the OpenAI Audio API.",
    "es": "Esta es una prueba de las capacidades multilingües de la API de audio de OpenAI.",
    "fr": "Ceci est un test des capacités multilingues de l'API audio d'OpenAI.",
    "de": "Dies ist ein Test der mehrsprachigen Fähigkeiten der OpenAI Audio API.",
    "ja": "これはOpenAI Audio APIの多言語機能のテストです。"
}

for lang, text in texts.items():
    speech_file_path = Path(__file__).parent / f"{lang}.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)