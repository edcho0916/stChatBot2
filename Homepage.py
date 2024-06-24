import streamlit as st

if "api_key" not in st.session_state:
    st.session_state.api_key = None

st.title("Welcome!!!")
st.title("💬 Chatbot For Teacher")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
st.write('왼쪽 사이드 바에서 1. PASSWORD 입력, 2. 상담 영역 선택.')

with st.sidebar:
    password = st.text_input("Password", key="chatbot_password", type="password")
    if not password :
        st.info('Please input your PASSWORD')
        st.stop()
    elif st.secrets['PASSWORD']==password:
        st.info('Select ChatBot and Input prompt')
        st.session_state.api_key = st.secrets['API_KEY']
    else:
        st.info('Input correct password!!!')
        st.stop()
    
