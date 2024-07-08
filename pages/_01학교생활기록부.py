from openai import OpenAI
import streamlit as st
import time

client = OpenAI(api_key = st.session_state.api_key)
assistant_ID = "asst_yhR5gQFgDoBNzoBGG3XUOzHB"

if "thread_ID_01" not in st.session_state:
    thread_01 = client.beta.threads.create()
    st.session_state.thread_ID_01 = thread_01.id

with st.sidebar:
    st.title("💬 학교생활기록부 ChatBot")
    st.write("참조파일 : 2024 생기부 기재요령 ")
    st.write(st.session_state.thread_ID_01)
    link = '<a href="https://https://drive.google.com/file/d/1VZf9J907jPdkIYIUKOSzMN5zYFb6gsbe/view?usp=sharing" target="_blank">학생부 매뉴얼 바로 가기</a>'
    st.markdown(link)

if "message_01" not in st.session_state:
    st.session_state["messages_01"] = [{"role": "assistant", "content": "안녕하세요. 학교생활기록부에 대해 궁금하신 점이 있으신가요?."}]

for msg in st.session_state.messages_01:
    st.chat_message(msg["role"]).write(msg["content"])
if prompt := st.chat_input():
    if not st.session_state.api_key:
       st.info("Please input your OpenAI API key to continue: at Homepage")
       st.stop()
    st.session_state.messages_01.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.beta.threads.messages.create(
    thread_id = st.session_state.thread_ID_01,
    role = "user",
    content = prompt,
     )

    run_01 = client.beta.threads.runs.create(
       thread_id = st.session_state.thread_ID_01, 
       assistant_id = assistant_ID
    )

    while True:
        run_01 = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_ID_01,
            run_id = run_01.id
        )
        if run_01.status=="completed":
            break
        else:
            time.sleep(2)
    thread_messages_01 = client.beta.threads.messages.list(st.session_state.thread_ID_01)
    msg = thread_messages_01.data[0].content[0].text.value
    print(thread_messages_01)
    st.session_state.messages_01.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
