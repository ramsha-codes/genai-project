import streamlit as st
import ollama

# Reset button
if st.button("Reset Chat"):
    st.session_state.messages = []
    st.success("Chat history has been reset!")

# Title
st.title("AI Chatbot - phi3:mini")

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

