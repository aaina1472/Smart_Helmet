import streamlit as st
from gtts import gTTS
import io
import time

st.set_page_config(page_title="Smart Helmet Simulator", layout="wide")
st.title("Smart Helmet Simulator 🏍️")

# Helper function to speak text
def speak(text):
    tts = gTTS(text=text, lang='en')
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    st.audio(audio_bytes, format='audio/mp3')

# ---------------- SPEED MONITORING ----------------
st.header("Speed Monitoring")
speed = st.slider("Current Speed (km/h)", 0, 150, 60)
st.write(f"Current Speed: {speed} km/h")

if speed > 80:
    st.warning("⚠️ Over-speeding! Slow down!")
    speak("Warning! Over-speeding!")

# ---------------- CRASH DETECTION ----------------
st.header("Crash Detection")
if st.button("Simulate Crash"):
    st.error("💥 Crash Detected! Alert Sent!")
    speak("Crash detected! Please help!")

# ---------------- SIMULATED ROUTE / DIRECTIONS ----------------
st.header("Navigation / Route Alerts (Simulated)")

start_location = st.text_input("Start Location", "Home")
end_location = st.text_input("Destination", "Office")

if st.button("Simulate Route"):
    st.success(f"Calculating route from {start_location} to {end_location}...")
    speak(f"Route calculation started from {start_location} to {end_location}.")
    
    # Simulated steps
    steps = [
        "Go straight for 500 meters",
        "Turn right at the next intersection",
        "Continue for 1 kilometer",
        "Your destination is on the left"
    ]
    
    for step in steps:
        st.info(step)
        speak(step)
        time.sleep(1)  # pause 1 sec between steps

st.write("⚡ Smart Helmet app simulates speed alerts, crash detection, and route guidance with working voice assistant using gTTS.")
