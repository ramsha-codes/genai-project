# Ollama Chatbot

This project is a **Chatbot** powered by the **phi3:mini** model from **Ollama**, built using **Streamlit**. The chatbot allows users to interact with the phi3:mini model and have real-time conversations. The conversations are stored persistently in a JSON file, allowing users to view previous interactions even after restarting or reloading the app.

---

## Features

- **Start a New Chat**: Allows users to begin a fresh conversation with the chatbot.
- **Reset Chat**: Clears the current chat history.
- **View Previous Conversations**: Displays past conversations in the sidebar, with the first user message as the topic.
- **Persistent Storage**: Conversations are saved in a local `conversations.json` file, ensuring that data persists even after a page reload or app restart.

---

## Requirements

- Python 3.7+
- Streamlit
- Ollama (for running the phi3:mini model)

You can install the necessary dependencies using `pip`:

pip install streamlit ollama

# How to Run

1. Clone the repository or download the files.

2. Install the dependencies:

   pip install -r requirements.txt


3. Run the Streamlit app:

   streamlit run app.py


# How It Works

The app uses Streamlit for the front-end interface and Ollama for the backend chatbot model.

Conversations are stored in a conversations.json file in the root directory. If the file doesn't exist, it will be automatically created.

Each conversation is saved as a list of messages and can be viewed in the sidebar, with the topic being the first message from the user.

# Features to Add

1. Improved Topic Generation: Currently, the topic is taken from the first user message. Future improvements can include generating a more concise and meaningful topic.

2. Cloud Storage: Storing conversations in a cloud service like Google Drive or AWS S3 to persist across multiple devices.

3. User Authentication: Adding user authentication to allow multiple users to have their own chat history.

# Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit pull requests. Here are a few ways you can contribute:

1. Fix bugs or improve the user interface

2. Add new features such as speech-to-text or voice chat

3. Improve documentation

# Credits

Streamlit: Framework for building the app UI.

Ollama: Provides the phi3:mini model for generating chatbot responses.

Creator of this project: Ramsha Imran (Intern @ Arch Technologies).