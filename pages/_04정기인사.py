from openai import OpenAI
import streamlit as st
import time

client = OpenAI(api_key = st.session_state.api_key)
assistant_ID = "asst_tuI9NcrwSve8KltxnqM8ZCav"


if "thread_ID_04" not in st.session_state:
    thread_04 = client.beta.threads.create()
    st.session_state.thread_ID_04 = thread_04.id

with st.sidebar:
    st.title("💬 정기인사 ChatBot")
    st.write("참조파일 : 24 교육공무원인사세부기준")
    st.write(st.session_state.thread_ID_04)


if "messages_04" not in st.session_state:
    st.session_state["messages_04"] = [{"role": "assistant", "content": "안녕하세요.교원인사, 정원, 계약제 채용에 대해 물어보세요."}]

for msg in st.session_state.messages_04:
    st.chat_message(msg["role"]).write(msg["content"])
if prompt := st.chat_input():
    if not st.session_state.api_key:
       st.info("Please input your OpenAI API key to continue: at Homepage")
       st.stop()
    st.session_state.messages_04.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.beta.threads.messages.create(
    thread_id = st.session_state.thread_ID_04,
    role = "user",
    content = prompt,
    )

    run_04 = client.beta.threads.runs.create(
        thread_id = st.session_state.thread_ID_04, 
        assistant_id = assistant_ID
    )

    while True:
        run_04 = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_ID_04,
            run_id = run_04.id
        )
        if run_04.status=="completed":
            break
        else:
            time.sleep(2)
    thread_messages_04 = client.beta.threads.messages.list(st.session_state.thread_ID_04)
    msg = thread_messages_04.data[0].content[0].text.value
    print(thread_messages_04)
    st.session_state.messages_04.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
