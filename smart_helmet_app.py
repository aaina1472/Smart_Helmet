import streamlit as st
import openrouteservice
from streamlit_folium import st_folium
import folium

st.title("Smart Helmet Simulator 🏍️ (Browser Voice)")

# ---------------- SPEED MONITORING ----------------
st.header("Speed Monitoring")
speed = st.slider("Current Speed (km/h)", 0, 150, 60)
st.write(f"Current Speed: {speed} km/h")

if speed > 80:
    st.warning("⚠️ Over-speeding! Slow down!")
    # Browser TTS
    st.markdown(f"""
    <script>
    var msg = new SpeechSynthesisUtterance("Warning! Over-speeding!");
    window.speechSynthesis.speak(msg);
    </script>
    """, unsafe_allow_html=True)

# ---------------- CRASH DETECTION ----------------
st.header("Crash Detection")
if st.button("Simulate Crash"):
    st.error("💥 Crash Detected! Alert Sent!")
    st.markdown(f"""
    <script>
    var msg = new SpeechSynthesisUtterance("Crash detected! Please help!");
    window.speechSynthesis.speak(msg);
    </script>
    """, unsafe_allow_html=True)

# ---------------- ROUTE AND DISTANCE ----------------
st.header("Route & Distance Calculator")
start = st.text_input("Start Location (lat,lon)", "28.6139,77.2090")  # Delhi
end = st.text_input("End Location (lat,lon)", "28.7041,77.1025")      # Nearby city

if st.button("Calculate Route"):
    try:
        start_coords = tuple(map(float, start.split(",")))
        end_coords = tuple(map(float, end.split(",")))

        client = openrouteservice.Client(key="eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImFiM2JmNTY1ZjQzNjRlMThhODE4NzEzOGFhOGI2Y2FjIiwiaCI6Im11cm11cjY0In0=")
        route = client.directions(coordinates=[start_coords[::-1], end_coords[::-1]])

        distance_m = route['routes'][0]['summary']['distance']
        duration_s = route['routes'][0]['summary']['duration']

        st.success(f"Distance: {distance_m/1000:.2f} km")
        st.success(f"Estimated Time: {duration_s/60:.2f} min")

        # Browser TTS for route
        st.markdown(f"""
        <script>
        var msg = new SpeechSynthesisUtterance(
            "Distance is {distance_m/1000:.2f} kilometers. Estimated time is {duration_s/60:.2f} minutes."
        );
        window.speechSynthesis.speak(msg);
        </script>
        """, unsafe_allow_html=True)

        # Interactive map
        route_coords = route['routes'][0]['geometry']['coordinates']
        route_coords = [(c[1], c[0]) for c in route_coords]

        m = folium.Map(location=start_coords, zoom_start=12)
        folium.Marker(start_coords, tooltip="Start").add_to(m)
        folium.Marker(end_coords, tooltip="End").add_to(m)
        folium.PolyLine(route_coords, color="blue", weight=5).add_to(m)

        st_folium(m, width=700, height=500)

    except Exception as e:
        st.error("Error calculating route. Check coordinates or API key.")
        st.write(e)
