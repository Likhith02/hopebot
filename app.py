# app.py

import streamlit as st
import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit Page Setup
st.set_page_config(page_title="HopeBot", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
        body {
            background: url('https://images.unsplash.com/photo-1517487881594-2787fef5ebf7?auto=format&fit=crop&w=1950&q=80');
            background-size: cover;
        }
        .main {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin: 50px auto;
            max-width: 700px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextArea textarea {
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        .stButton button {
            background-color: #4caf50;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)



st.title("🌟 HopeBot – Your AI Friend for Tough Days")
st.subheader("Because even the strongest students feel lost sometimes 💛")
st.write("Feeling low, anxious, or just unsure what to do next? HopeBot listens. You type, it reflects, it supports.")


# User Input
st.markdown("#### 💬 Quick Help Prompts")
selected_prompt = st.selectbox(
    "Choose how you're feeling (optional):",
    (
        "Select a feeling...",
        "😔 I feel lost in life and don’t know where I’m going.",
        "💼 I’m stressed about finding a job and building a future.",
        "💔 I feel like I’m failing and not good enough.",
        "✨ I just need some motivation or something kind today."
    )
)

if selected_prompt != "Select a feeling...":
    user_input = selected_prompt
else:
    user_input = st.text_area("📝 What's on your mind today?", height=150)



# Get AI response
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = api_key)
def get_hopebot_reply(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a kind and supportive AI named HopeBot. Your job is to comfort and motivate international students who are feeling lost, tired, or uncertain about life."},
            {"role": "user", "content": message}
        ],
        temperature=0.8,
        max_tokens=300
    )
    return response.choices[0].message.content

# When user clicks send
if st.button("Send to HopeBot"):
    if user_input.strip() == "":
        st.warning("Please type something first.")
    else:
        with st.spinner("HopeBot is thinking..."):
            reply = get_hopebot_reply(user_input)
            st.success("HopeBot says:")
            st.write(reply)
