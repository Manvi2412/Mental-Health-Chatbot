# app.py
import streamlit as st
from chatbot import get_bot_response
import pandas as pd
import plotly.express as px

# App settings
st.set_page_config(page_title="Mindful — Mental Health Chatbot", page_icon="🧠", layout="centered")

st.title("🧠 Mindful — Mental Health Chatbot")
st.markdown("Kind, simple support. No medical advice. If you’re in danger, call your local emergency number.")

# Session state for conversation and mood tracking
if "messages" not in st.session_state:
    st.session_state.messages = []
if "mood_log" not in st.session_state:
    st.session_state.mood_log = []

# User input
user_input = st.text_input("You:", "")

col1, col2 = st.columns([1, 4])
with col1:
    mood_toggle = st.toggle("📊 View Mood Trends")
with col2:
    send_button = st.button("Send")

# Send message
if send_button and user_input.strip():
    bot_reply, mood = get_bot_response(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", bot_reply))
    st.session_state.mood_log.append({"message": user_input, "mood": mood})

# Display conversation
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Bot:** {msg}")

# Mood trends
if mood_toggle and st.session_state.mood_log:
    df = pd.DataFrame(st.session_state.mood_log)
    fig = px.histogram(df, x="mood", title="Mood Trend", color="mood")
    st.plotly_chart(fig)

# Clear conversation
if st.button("Clear Conversation"):
    st.session_state.messages.clear()
    st.session_state.mood_log.clear()
