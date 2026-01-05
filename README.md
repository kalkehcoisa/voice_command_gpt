# 🎙️ Conversando por Voz com ChatGPT usando Whisper e Python 3.14

Este projeto demonstra a construção de um sistema de conversação por voz utilizando **Speech-to-Text (STT)** e **Text-to-Speech (TTS)**, integrando o **Whisper** e a **API da OpenAI (ChatGPT)** com **Python 3.14**.

A aplicação é capaz de:

1. Gravar áudio via microfone  
2. Transcrever a fala para texto usando Whisper  
3. Enviar a transcrição para o ChatGPT  
4. Receber a resposta em texto  
5. Converter a resposta em áudio utilizando Google Text-to-Speech (gTTS)  

Tudo isso permitindo interações naturais, multi‑idioma e orientadas por voz 🚀

---

## 🧠 Contexto do Desafio (DIO)

Este projeto faz parte de um **Desafio de Projeto da DIO**, cujo objetivo é aplicar na prática conceitos de:

- Speech-to-Text  
- Integração com modelos de linguagem (LLMs)  
- Text-to-Speech  
- Uso de APIs de IA em Python  

A proposta é criar um projeto funcional e extensível, que possa ser utilizado como **item de portfólio no GitHub**, servindo como base para futuras evoluções.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.14**
- **Whisper (OpenAI)** – Transcrição de áudio
- **OpenAI API (ChatGPT)** – Geração de respostas
- **Google Text-to-Speech (gTTS)** – Síntese de voz
- **sounddevice** – Captura de áudio do microfone
- **NumPy / SciPy** – Manipulação de áudio
- **ffmpeg / ffplay** – Reprodução de áudio

---

## 📂 Estrutura do Projeto

```
.
├── audio_text_gpt.py      # Script principal
├── requirements.txt       # Dependências do projeto
├── command.wav            # Áudio gravado
├── command.txt            # Texto transcrito pelo Whisper
├── gpt_response.txt       # Resposta gerada pelo ChatGPT
├── audio_response.mp3     # Áudio com a resposta sintetizada
└── .keys                  # Arquivo com a chave da OpenAI (não versionar)
```

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Criar e ativar um ambiente virtual

```bash
python3.14 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

> ⚠️ É necessário ter o **ffmpeg** instalado e disponível no PATH do sistema.

---

## 🔑 Configuração da API Key

Crie um arquivo chamado **`.keys`** na raiz do projeto contendo apenas sua chave da OpenAI:

```
SUA_OPENAI_API_KEY_AQUI
```

⚠️ **Nunca versionar este arquivo**.

---

## ▶️ Como Executar

### Execução completa (gravação → transcrição → resposta → áudio)

No arquivo `audio_text_gpt.py`, utilize o fluxo completo:

```python
command_file = record()
transcription = transcribe(command_file=command_file)
chatgpt_response = ask_gpt(transcription=transcription)
pronounce_response(text=chatgpt_response)
```

Depois execute:

```bash
python audio_text_gpt.py
```

Fale no microfone, pressione **Enter** para finalizar a gravação e aguarde a resposta em áudio.

---

## 🧪 Execução Parcial (modo teste)

O projeto permite reutilizar arquivos já gerados:

- `command.wav`
- `command.txt`
- `gpt_response.txt`

Isso facilita testes locais sem a necessidade de gravar áudio ou consumir a API a cada execução.

---

## 🚀 Possíveis Evoluções

- Interface gráfica (Tkinter, PyQt ou Web)
- Detecção automática de idioma
- Conversação contínua por voz
- Streaming de áudio em tempo real
- Deploy como aplicação desktop ou serviço
- Integração com assistentes virtuais ou IoT

---

## 📚 Links Úteis

- 📄 Artigo explicativo do projeto:  
  **Conversando Por Voz Com o ChatGPT Utilizando Whisper (OpenAI) e Python**

- 💻 Código-base do desafio no Google Colab:  
  https://bit.ly/41XfKaM

- 🎥 Live do Lab no YouTube (DIO):  
  https://bit.ly/44e9Nrw

---

## 📌 Observação Final

Este projeto tem fins educacionais e demonstra, de forma prática, como combinar **IA generativa**, **processamento de áudio** e **Python** para criar soluções modernas de interação humano–máquina.

