
# Voice Cloning + Emotion Response Bot 
import gradio as gr
import requests
import os
from pydub import AudioSegment
from dotenv import load_dotenv
import json
import pyttsx3
import uuid

load_dotenv()

# === CONFIG ===
SAMBA_API_KEY = os.getenv("SAMBA_API_KEY")
SAMBA_API_URL = "https://api.sambanova.ai/v1"  # Adjust if different

# === Emotion Detection (placeholder) ===
def detect_emotion(audio_path):
    # TODO: Replace with actual emotion detection model
    return "sad"

# === SambaNova GPT Response ===
def generate_response(transcript, emotion):
    headers = {
        "Authorization": f"Bearer {SAMBA_API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"The user sounds {emotion}. Respond empathetically to this message: '{transcript}'"
    data = {
        "model": "Llama-4-Maverick-17B-128E-Instruct",  # Replace with the actual model ID if needed
        "messages": [
            {"role": "system", "content": "You are an empathetic AI therapist."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(SAMBA_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Sorry, I couldn't generate a response."

# === pyttsx3 TTS (Offline) ===
def synthesize_speech(text):
    engine = pyttsx3.init()
    output_file = f"output_{uuid.uuid4().hex}.mp3"
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    return output_file

# === Main Function ===
def process(audio_path):
    if audio_path is None:
        return "No audio recorded", "", "", None

    audio_segment = AudioSegment.from_file(audio_path)
    audio_segment.export("input.wav", format="wav")

    # TODO: Replace with real transcription like Whisper if needed
    transcript = "This is a test transcription."

    emotion = detect_emotion("input.wav")
    gpt_response = generate_response(transcript, emotion)
    audio_output = synthesize_speech(gpt_response)

    return transcript, emotion, gpt_response, audio_output

# === Gradio Interface ===
iface = gr.Interface(
    fn=process,
    inputs=gr.Audio(sources=["microphone"], type="filepath", label="Speak your message"),
    outputs=[
        gr.Textbox(label="Transcript"),
        gr.Textbox(label="Detected Emotion"),
        gr.Textbox(label="AI Response"),
        gr.Audio(label="AI Voice Response")
    ],
    title="Voice Cloning + Emotion Response Bot (SambaNova + pyttsx3)",
    description="🎙️ Speak something. The bot detects your emotion, replies using SambaNova GPT, and speaks using offline pyttsx3 TTS."
)

iface.launch()
