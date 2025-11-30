import streamlit as st
import time

st.set_page_config(page_title="Smart Helmet Simulator", layout="wide")
st.title("Smart Helmet Simulator 🏍️")

# ---------------- SPEED MONITORING ----------------
st.header("Speed Monitoring")
speed = st.slider("Current Speed (km/h)", 0, 150, 60)
st.write(f"Current Speed: {speed} km/h")

if speed > 80:
    st.warning("⚠️ Over-speeding! Slow down!")
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

# ---------------- SIMULATED ROUTE / DIRECTIONS ----------------
st.header("Navigation / Route Alerts (Simulated)")

start_location = st.text_input("Start Location", "Home")
end_location = st.text_input("Destination", "Office")

if st.button("Simulate Route"):
    st.success(f"Calculating route from {start_location} to {end_location}...")
    st.markdown("""
    <script>
    var msg = new SpeechSynthesisUtterance("Route calculation started from {} to {}.");
    window.speechSynthesis.speak(msg);
    </script>
    """.format(start_location, end_location), unsafe_allow_html=True)
    
    # Simulate steps
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
        time.sleep(2)  # pause 2 sec between steps

st.write("⚡ This Smart Helmet app simulates speed alerts, crash detection, and route guidance with voice feedback—all working directly in your browser.")
