import streamlit as st
import google.generativeai as genai


def side_bar():
    google_api_key = st.sidebar.text_input("Google API Key", placeholder="Enter your Google API Key")
    st.session_state['google_api_key'] = str(google_api_key)
    
    model_name = st.sidebar.selectbox("Which model do you want to use?",["gemini-2.0-flash-exp", "gemini-1.5-flash", "gemini-1.5-flash-8b","gemini-1.5-pro"],)
    st.session_state['model_name'] = str(model_name)

    additional_information = st.sidebar.text_area("Additional Instructions", placeholder="Enter additional information")
    st.session_state['additional_information'] = str(additional_information)
 
    # st.sidebar.write(st.session_state['additional_information'])
    # st.sidebar.write(st.session_state['google_api_key'])
    # st.sidebar.write(st.session_state['model_name'])
    # st.sidebar.write(st.session_state['chat_history'])