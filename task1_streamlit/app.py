import streamlit as st
import ollama

# Title
st.title("AI Chatbot - phi3:mini")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

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
