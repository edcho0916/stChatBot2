import streamlit as st

if "password" not in st.session_state:
    st.session_state.password = None

st.title("Welcome!!!")
st.title("💬 Chatbot For Teacher")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
st.write('왼쪽 사이드 바에서 1. PASSWORD 입력, 2. 상담 영역 선택.')

with st.sidebar:
    password = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value=st.session_state.api_key)
    if not password :
        st.info('Please input your PASSWORD')
        st.stop()
    elif st.secrets['PASSWORD']==password:
        st.info('Select ChatBot and Input prompt')
        st.session_state.api_key = st.secrets{'API_KEY']
    else:
        st.info('Input correct password!!!')
        st.stop()
    
