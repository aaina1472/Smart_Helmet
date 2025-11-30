import streamlit as st
import time

st.title("Smart Helmet Simulator 🏍️")

# ---------------- SPEED MONITORING ----------------
st.header("Speed Monitoring")
speed = st.slider("Current Speed (km/h)", 0, 150, 60)
st.write(f"Current Speed: {speed} km/h")

if speed > 80:
    st.warning("⚠️ Over-speeding! Slow down!")
    # Browser TTS fallback
    st.markdown("""
    <script>
    var msg = new SpeechSynthesisUtterance("Warning! Over-speeding!");
    window.speechSynthesis.speak(msg);
    </script>
    """, unsafe_allow_html=True)

# ---------------- CRASH DETECTION ----------------
st.header("Crash Detection")
if st.button("Simulate Crash"):
    st.error("💥 Crash Detected! Alert Sent!")
    st.markdown("""
    <script>
    var msg = new SpeechSynthesisUtterance("Crash detected! Please help!");
    window.speechSynthesis.speak(msg);
    </script>
    """, unsafe_allow_html=True)

# ---------------- SIMULATED ROUTE ----------------
st.header("Navigation / Route Alerts (Simulated)")
start = st.text_input("Start Location", "Home")
end = st.text_input("Destination", "Office")

if st.button("Simulate Route"):
    st.success(f"Route from {start} to {end}")
    steps = [
        "Go straight for 500 meters",
        "Turn right at the next intersection",
        "Continue for 1 kilometer",
        "Your destination is on the left"
    ]
    for step in steps:
        st.info(step)
        st.markdown(f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{step}");
        window.speechSynthesis.speak(msg);
        </script>
        """, unsafe_allow_html=True)
        time.sleep(1)
