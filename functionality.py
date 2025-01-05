import google.generativeai as genai
import os
import streamlit as st

def load_chat_history():
    model = genai.GenerativeModel(model_name=st.session_state['model_name'],
      system_instruction=st.session_state['additional_information'])
    chat = model.start_chat(
            history=st.session_state['chat_history']
    )
    return chat


def get_gemini_response(question):
    genai.configure(api_key=st.session_state['google_api_key'])
    chat = load_chat_history()
    response = chat.send_message(question)
    return response