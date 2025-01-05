import streamlit as st
import os
from main_page import main_page
from sidebar import side_bar

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'google_api_key' not in st.session_state:
    st.session_state['google_api_key'] = None

if 'model_name' not in st.session_state:
    st.session_state['model_name'] = "gemini-2.0-flash-exp"

if 'additional_information' not in st.session_state:
    st.session_state['additional_information'] = "You are helpful assistant."

st.header("ChatBot")

 
side_bar()
main_page()
