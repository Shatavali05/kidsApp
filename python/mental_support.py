import streamlit as st
import ollama
import datetime
from gtts import gTTS
import os
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import io
# Set page title and layout
st.set_page_config(
    page_title="🌈 Mindful Buddy - Your friend- It's you", 
    layout="centered"
)

# Custom CSS for a Child-Friendly Look
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
        }
        h1 {
            color: #ff5e62;
            text-align: center;
            font-size: 2.8em;
            font-weight: bold;
        }
        .stChatMessage {
            background-color: rgba(255, 255, 255, 0.85);
            border-radius: 15px;
            padding: 12px;
            margin: 5px 0;
            font-size: 1.1em;
        }
        .stButton>button {
            background: linear-gradient(to right, #ff9966, #ff5e62);
            color: white;
            border-radius: 12px;
            font-size: 18px;
            padding: 10px 18px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(to right, #ff5e62, #ff9966);
        }
        .stSelectbox label {
            font-size: 1.2em;
            font-weight: bold;
        }
        .mood-log {
            border-radius: 8px;
            background: #fddde6;
            padding: 10px;
            margin: 5px 0;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session states
st.session_state.setdefault("conversation_history", [])
st.session_state.setdefault("mood_history", [])

# Function to generate AI response
def generate_response(user_input, mood):
    st.session_state["conversation_history"].append({"role": "user", "content": user_input})

    # Adjust prompt based on mood
    mood_prompt = f"My current mood is {mood}. Please respond kindly and positively."
    messages = st.session_state["conversation_history"] + [{"role": "user", "content": mood_prompt}]

    try:
        response = ollama.chat(model="gemma:2b", messages=messages)
        ai_response = response["message"]["content"]
    except Exception:
        ai_response = "⚠ Oops! I couldn't respond. Try again!"

    st.session_state["conversation_history"].append({"role": "assistant", "content": ai_response})
    return ai_response

# Function to generate a positive affirmation
@st.cache_data
def generate_affirmation():
    prompt = "Give me a fun and encouraging positive affirmation for kids."
    try:
        response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception:
        return "⚠ I couldn't fetch an affirmation. Try again later!"

# Function to generate a simple guided meditation
@st.cache_data
def generate_meditation_guide():
    prompt = "Create a 3-minute guided meditation for relaxation in a kid-friendly way."
    try:
        response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception:
        return "⚠ Unable to generate meditation. Try again later!"

# Function to generate voice audio
def generate_voice(text, filename="audio.mp3"):
    tts = gTTS(text, lang="en", slow=False)
    tts.save(filename)
    return filename

# Title
st.title("🌈 Mindful Buddy - Your Friendly Chatbot")

# Mood Selection
mood_options = {
    "😊 Happy": "happy",
    "😢 Sad": "sad",
    "😠 Angry": "angry",
    "😟 Anxious": "anxious",
    "😌 Relaxed": "relaxed",
    "😴 Tired": "tired"
}
selected_mood = st.selectbox("How are you feeling today?", list(mood_options.keys()))

# Log Mood
if st.button("📖 Log Mood"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    st.session_state["mood_history"].append({"mood": selected_mood, "time": timestamp})
    st.success(f"✅ Mood '{selected_mood}' logged!")

# Display Mood History
if st.session_state["mood_history"]:
    st.subheader("📅 Mood History")
    for entry in reversed(st.session_state["mood_history"][-5:]):
        st.markdown(f"<div class='mood-log'>🕒 {entry['time']} - {entry['mood']}</div>", unsafe_allow_html=True)

# Chat Section
st.subheader("💬 Chat with Mindful Buddy")

# Display chat history
for msg in st.session_state["conversation_history"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(f"🗣 *You:* {msg['content']}")
    else:
        st.chat_message("assistant").markdown(f"🤖 *Buddy:* {msg['content']}")

# User input
user_message = st.chat_input("What's on your mind?")

# Process user message
if user_message and user_message.strip():
    with st.spinner("💭 Thinking..."):
        ai_response = generate_response(user_message, mood_options[selected_mood])
        st.chat_message("assistant").markdown(f"🤖 *Buddy:* {ai_response}")
else:
    if user_message:
        st.warning("⚠ Please type a message before sending.")

# Buttons for Affirmations & Meditation Guide
col1, col2 = st.columns(2)

with col1:
    if st.button("💖 Positive Affirmation"):
        affirmation = generate_affirmation()
        st.success(f"✨ *Affirmation:* {affirmation}")
        
        # Generate and play affirmation audio
        audio_file = generate_voice(affirmation, "affirmation.mp3")
        st.audio(audio_file, format="audio/mp3")

with col2:
    if st.button("🧘‍♂ Quick Meditation"):
        meditation_guide = generate_meditation_guide()
        st.success(f"🌿 *Meditation Guide:* {meditation_guide}")
        
        # Generate and play meditation audio
        audio_file = generate_voice(meditation_guide, "meditation.mp3")
        st.audio(audio_file, format="audio/mp3")

# 🎨 Drawing Pad Section
st.subheader("🎨 Express Yourself - Draw Your Feelings!")

# Color Picker for Stroke Color
selected_color = st.color_picker("🎨 Pick a Color", "#000000")

canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",  # Transparent background
    stroke_width=5,
    stroke_color=selected_color,  # Use selected color
    background_color="#F0F0F0",  # Light gray background
    width=400,
    height=300,
    drawing_mode="freedraw",
    key="canvas",
)

# Save the drawing as an image
if st.button("💾 Save Drawing"):
    if canvas_result.image_data is not None:
        img = Image.fromarray((canvas_result.image_data * 255).astype(np.uint8))
        img_buffer = io.BytesIO()
        img.save(img_buffer, format="PNG")
        st.download_button(label="📥 Download Your Drawing", data=img_buffer.getvalue(), file_name="drawing.png", mime="image/png")
    else:
        st.warning("⚠ No drawing found! Please draw something first.")