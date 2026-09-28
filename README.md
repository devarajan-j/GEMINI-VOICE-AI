# GEMINI-VOICE-AI

Gemini Voice AI chatbot project.

## Files
- `index.html` - frontend chatbot interface
- `app.py` - Flask backend and Gemini API endpoint
- `requirements.txt` - Python dependencies
- `.env` - local Gemini configuration
- `.env.example` - environment template

## Setup
1. Install Python 3.10+.
2. Create a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Put your Gemini API key in `.env`.
5. Run `python app.py`.
6. Open `http://127.0.0.1:5000`.

## Features
Text chat, voice input, text-to-speech, chat history, theme switching, responsive dashboard, typing indicator, copy and speak controls.

## Security
Keep `.env` private. Do not commit real API keys to source control.
