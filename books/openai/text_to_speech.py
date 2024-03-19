# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from pathlib import Path
from openai import OpenAI


client = OpenAI(api_key="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")

speech_file_path = "./speech.mp3"

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)