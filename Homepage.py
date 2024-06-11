import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    
st.title("💬 Chatbot For Teacher")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
st.write('왼쪽 사이드바에서 해당 영역을 선택하고 OpenAI사의 APIKEY를 입력해 주세요. ')

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
