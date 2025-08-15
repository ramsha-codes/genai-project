import streamlit as st
import ollama

# Add custom CSS for buttons
st.markdown("""
    <style>
        .stButton > button {
            background-color: #4E6F7D;  # Green for 'Start New Chat' button
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px 24px;
        }
        .stButton > button:hover {
            background-color: #4F9BA8;  # Darker green on hover
        }
        
        .stButton > button:nth-child(2) {
            background-color: #f44336;  # Red for 'Reset Chat' button
            color: white;
        }
        
        .stButton > button:nth-child(2):hover {
            background-color: #e53935;  # Darker red on hover
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("___")  # Horizontal separator

# Title
st.title("AI Chatbot - phi3:mini")
st.markdown("By Ramsha Imran (Intern @ Arch Technologies)")

st.sidebar.title("Previous Conversations")
if "conversations" not in st.session_state:
    st.session_state.conversations = []

# Start a new chat
if st.button("Start New Chat"):
    # Save current conversation into the history before starting a new one
    if st.session_state.messages:
        st.session_state.conversations.append(st.session_state.messages)
    st.session_state.messages = []

# Reset button
if st.button("Reset Chat"):
    st.session_state.messages = []
    st.success("Chat history has been reset!")

# Display previous conversations in the sidebar
for idx, prev_chat in enumerate(st.session_state.conversations):
    with st.sidebar.expander(f"Conversation {idx + 1}"):
        for msg in prev_chat:
            st.markdown(f"**{msg['role']}:** {msg['content']}")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Scrollable area for the chat history
with st.container():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

st.markdown("___")  # Horizontal separator

# User input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to phi3:mini
    with st.chat_message("assistant"):
        response = ollama.chat(
            model="phi3:mini",
            messages=st.session_state.messages
        )
        reply = response['message']['content']
        st.markdown(reply)

    # Save assistant reply
    st.session_state.messages.append({"role": "assistant", "content": reply})

