import streamlit as st
import requests

# URL of your FastAPI server
API_URL = "http://localhost:8000/llm"


st.title("🌐 Groq Translator")

# User input
text = st.text_area("Enter text in English:")
lang = st.selectbox("Translate to:", ["French", "Spanish", "German", "Hindi", "Chinese", "Japanese"])

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Make POST request to FastAPI
        payload = {"text": text, "lang": lang}
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                translation = response.json()["translation"]
                st.success("✅ Translation Complete!")
                st.text_area("Translated Text:", translation, height=150)
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to API: {e}")
