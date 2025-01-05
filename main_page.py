import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from functionality import get_gemini_response, load_chat_history


def main_page():
    try:
        user_question = st.chat_input("Input: ", key="input")

        for chat_history in st.session_state.chat_history:
            if chat_history["role"] == "user":    
                with st.chat_message("user"):
                    st.markdown(chat_history["parts"])
            else:
                with st.chat_message("assistant"):
                    st.markdown(chat_history["parts"])
        
        if user_question : 
                with st.chat_message("user"):
                    st.write(user_question)
                    st.session_state['chat_history'].append({"role": "user", "parts": user_question})
                    load_chat_history()
                
                with st.chat_message("assistant"):
                    with st.spinner("Generating..."):
                        response = get_gemini_response(user_question)
                        st.write(response.text)
                        st.session_state['chat_history'].append({"role": "model", "parts": response.text})
                        load_chat_history()

    except Exception as e:
        st.error(e)