import streamlit as st

if "api_key" not in st.session_state:
     st.session_state.api_key = None

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value=st.session_state.api_key)
    if not openai_api_key:
        st.info('Please input your OpenAI API key')
        st.stop()
    else:
        st.info('Select ChatBot and Input prompt')
        st.session_state.api_key = openai_api_key
    
st.title("💬 Chatbot For Teacher")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
st.write('왼쪽 사이드바에서 해당 영역을 선택하고 OpenAI사의 APIKEY를 입력해 주세요. ')

