import streamlit as st
import ollama
import json
import os

# Check if the file exists, if not create it
file_path = 'conversations.json'

if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        json.dump([], f)  

# Load previous conversations from the JSON file
with open(file_path, 'r') as f:
    conversations = json.load(f)

st.set_page_config(page_title="Ollama Chatbot")

# Ensure conversations are stored in the session state
if "conversations" not in st.session_state:
    st.session_state.conversations = conversations  # Load previous conversations into session state
if "messages" not in st.session_state:
    st.session_state.messages = []  # Initialize the current chat if not already

# Add a new conversation to the file
if st.session_state.messages:
    # Save current conversation into the history before starting a new one
    conversations.append(st.session_state.messages)
    with open(file_path, 'w') as f:
        json.dump(conversations, f)  # Save the new conversations

# Custom CSS for buttons
st.markdown("""
    <style>
        .stButton > button {
            background-color: #4E6F7D;  
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px 24px;
        }
        .stButton > button:hover {
            background-color: #4F9BA8;  
        }
        
        .stButton > button:nth-child(2) {
            background-color: #f44336;  
            color: white;
        }
        
        .stButton > button:nth-child(2):hover {
            background-color: #e53935;  
        }
    </style>
""", unsafe_allow_html=True)

# Create 2 columns: one for the 'Start New Chat' button (left) and one for 'Reset Chat' button (right)
col1, col2 = st.columns([3, 1])  # 3 for the 'Start New Chat' button and 1 for the 'Reset Chat' button

# Place 'Start New Chat' button in the first column (left side)
with col1:
    if st.button("Start New Chat"):
        # Save current conversation into the history before starting a new one
        if st.session_state.messages:
            st.session_state.conversations.append(st.session_state.messages)
        st.session_state.messages = []

# Place 'Reset Chat' button in the second column (right side)
with col2:
    if st.button("Reset Chat"):
        st.session_state.messages = []
        st.success("Chat history has been reset!")

st.markdown("___")  # Horizontal separator

# Title
st.title("AI Chatbot - phi3:mini")
st.markdown("By Ramsha Imran (Intern @ Arch Technologies)")


# Display previous conversations in the sidebar
st.sidebar.title("Previous Conversations")
for idx, prev_chat in enumerate(st.session_state.conversations):
    conversation_topic = prev_chat[0]["content"][:50]  # First user message as topic
    with st.sidebar.expander(f"{conversation_topic}"):
        for msg in prev_chat:
            st.markdown(f"**{msg['role']}:** {msg['content']}")

# Current chat history
with st.container():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

st.markdown("___")  # Horizontal separator

# User input for new messages
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to phi3:mini and get response
    with st.chat_message("assistant"):
        response = ollama.chat(
            model="phi3:mini",
            messages=st.session_state.messages
        )
        reply = response['message']['content']
        st.markdown(reply)

    # Save assistant reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
