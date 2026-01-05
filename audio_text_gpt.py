import os
import subprocess

import numpy as np
from openai import OpenAI
import sounddevice as sd
import whisper
from gtts import  gTTS
from scipy.io.wavfile import read, write

RECORD_FILE = 'command.wav'
SAMPLE_RATE = 16000
TRANSCRIBED_FILE = 'command.txt'
RESPONSE_TEXT = 'gpt_response.txt'


def record():
    print("Gravando... Pressione Enter para parar")

    recording = []

    def callback(indata, frames, time, status):
        recording.append(indata.copy())

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, callback=callback, dtype="int16"):
        input()

    if recording:
        audio = np.concatenate(recording)
        write(RECORD_FILE, SAMPLE_RATE, audio)
        print("Gravado com sucesso!")
        return RECORD_FILE

    print("Falha: nenhum som foi registrado.")
    return None


def transcribe(command_file):
    # Selecione o modelo do Whisper que melhor atenda às suas necessidades:
    # https://github.com/openai/whisper#available-models-and-languages
    model = whisper.load_model("small")

    # Transcreve o audio gravado anteriormente.
    result = model.transcribe(command_file, fp16=False, language='Portuguese')
    transcription = result["text"]
    with open(TRANSCRIBED_FILE, 'w') as file:
        file.write(transcription)
    print(transcription)
    return transcription


def ask_gpt(transcription):
    # Configura a chave de API da OpenAI usando o valor no arquivo .keys
    with open(".keys", "r") as f:
        API_KEY = f.read().strip()

    # Envia uma requisição à API do ChatCompletion usando o modelo GPT-3.5 Turbo
    # Lembrando que, a variável 'transcription' contém a transcrição do nosso áudio.
    client = OpenAI(api_key=API_KEY)
    response = client.responses.create(
        model="gpt-4o-mini",
        input=transcription
    )

    # Obtém a resposta gerada pelo ChatGPT
    chatgpt_response = response.output_text
    with open(RESPONSE_TEXT, 'w') as file:
        file.write(chatgpt_response)
    print(chatgpt_response)
    return chatgpt_response


def play_audio(path):
    subprocess.run(
        ["ffplay", "-nodisp", "-autoexit", path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def pronounce_response(text):
    # Cria um objeto gTTS com a resposta gerada pelo ChatGPT e a língua que será sintetizada em voz (variável "language").
    gtts_object = gTTS(text=chatgpt_response, lang='pt-br', slow=False)

    # Salva o áudio da resposta no arquivo especificado (pasta padrão do Google Colab)
    response_audio = os.path.join(os.path.dirname(__file__), 'audio_response.mp3')
    gtts_object.save(response_audio)

    play_audio(response_audio)


if __name__ == '__main__':
    command_file = record()
    # command_file = RECORD_FILE
    transcription = transcribe(command_file=command_file)
    # with open(TRANSCRIBED_FILE, 'r') as file:
    #     transcription = file.read().strip()
    chatgpt_response = ask_gpt(transcription=transcription)
    # with open(RESPONSE_TEXT, 'r') as file:
    #     chatgpt_response = file.read().strip()
    pronounce_response(text=chatgpt_response)
