# Task 1 — Local LLM Chat (Streamlit + Ollama)

## Quick start
1) Create venv: 
   python3 -m venv .venv && source .venv/bin/activate

2) Install dependencies:
   python -m pip install -r requirements.txt

3) Pull a model (example: mistral):
   ollama pull mistral

4) Run the app:
   python -m streamlit run app.py

Notes:
- Use  on Mac for speed and stability.
- The app lists only installed models (via NAME         ID              SIZE      MODIFIED       
phi3:mini    4f2222927938    2.2 GB    16 minutes ago    ).
