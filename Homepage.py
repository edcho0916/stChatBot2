import streamlit as st
from openai import OpenAI

if "api_key" not in st.session_state:
    st.session_state.api_key = None

st.title("Welcome!!!")
st.title("💬 Chatbot For Teacher")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
st.write('왼쪽 사이드 바에서 1. API key 입력, 2. 상담 영역 선택.')

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value=st.session_state.api_key)
    if not openai_api_key:
        st.info('Please input your OpenAI API key')
        st.stop()
    else:
        st.info('Select ChatBot and Input prompt')
        st.session_state.api_key = openai_api_key
    
