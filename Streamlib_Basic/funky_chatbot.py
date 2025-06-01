import streamlit as st
from groq import Groq

# API Key (replace with st.secrets for safety if needed)
GROQ_API_KEY = "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"

# Groq Client
client = Groq(api_key=GROQ_API_KEY)

# Page Setup
st.set_page_config(page_title="Serious Guy Chatbot", layout="centered")
st.markdown("<h1 style='text-align: center;'>🤖 Serious Guy Your Seriousst Friend</h1>", unsafe_allow_html=True)

# Session state setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "system",
            "content": "You are a very serious , your name is serious Guy. Whatever user asks, you reply in a very serious and polite way."
        }
    ]
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Chat bubble CSS
st.markdown("""
    <style>
        .user-message {
            background-color: #DCF8C6;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 8px;
            margin-left: auto;
            max-width: 70%;
        }
        .bot-message {
            background-color: #F1F0F0;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 8px;
            margin-right: auto;
            max-width: 70%;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

# Display chat history
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-container'><div class='user-message'><b>👤 You:</b><br>{msg['content']}</div></div>", unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f"<div class='chat-container'><div class='bot-message'><b> Serious Guy:</b><br>{msg['content']}</div></div>", unsafe_allow_html=True)

# Input with button
with st.form(key="chat_form", clear_on_submit=True):
    user_text = st.text_input("💬 Type your message:", value="", placeholder="Say something funny...")
    submitted = st.form_submit_button("Send")

# If Send is clicked
if submitted and user_text.strip():
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": user_text.strip()})

    with st.spinner("🤔 Serious Guy is thinking..."):
        response = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=st.session_state.chat_history,
            max_tokens=500,
            temperature=1.2
        )
        reply = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

    