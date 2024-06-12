from openai import OpenAI
import streamlit as st
import time

with st.sidebar:
    st.title("💬 학교생활기록부챗봇")
    st.write("참조파일 : 2024 생기부 기재요령 ")
    st.text(st.session_state.api_key)

    client = OpenAI(api_key = st.session_state.api_key)
    assistant_ID = 'asst_yhR5gQFgDoBNzoBGG3XUOzHB'

    def assistantsID(chatbotName):
        my_assistants = client.beta.assistants.list(
        order="desc",
        limit="20",
        )
        time.sleep(2)
        count = my_assistants.data.count('Assistant')
        x=0
        while x <= count:
            if my_assistants.data[x].name == chatbotName:
                return my_assistants.data[x].id

    assistant_ID = assistantsID('학교생활기록부챗봇')
st.wirte(assistant_ID)
