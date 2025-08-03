
# Voice Emotion AI Bot 🎙️🧠

This project is a voice-based AI bot that:
1. Records your voice 🎤
2. (Stub) Detects your emotional tone 😔😊
3. Sends a prompt to **SambaNova GPT** for an empathetic response 🧠
4. Converts the AI response into speech using **offline pyttsx3 TTS** 🔊

---

## Features 🚀
- ✅ Uses SambaNova GPT via API for intelligent responses
- ✅ Offline speech synthesis (no ElevenLabs needed)
- ✅ Simple Python code using `gradio`, `requests`, and `pyttsx3`

---

## Requirements 📦

Install dependencies:

```bash
pip install -r requirements.txt
```

Required environment variable:

```bash
SAMBA_API_KEY=your_sambanova_api_key
```

---

## Run Locally 💻

```bash
python app.py
```

---

## File Structure 📁

- `app.py`: Main Gradio app
- `requirements.txt`: Dependencies list
- `.env`: Add your SambaNova API key here

---

## Notes 📌
- Emotion detection and transcription are placeholders. You can integrate real models like Whisper (OpenAI) and FER (Facial/Voice Emotion Recognition).
- Audio output is stored as temporary MP3 via `pyttsx3`

---

## Credits 🙏

Built by Khushal ❤️
