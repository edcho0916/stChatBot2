from openai import OpenAI
import streamlit as st
import time

client = OpenAI(api_key = st.session_state.api_key)
assistant_ID = "asst_bdikdGec9bkrpt3b4EQO5DZD"


if "thread_ID_06" not in st.session_state:
    thread_06 = client.beta.threads.create()
    st.session_state.thread_ID_06 = thread_06.id

with st.sidebar:
    st.title("💬 학교폭력 ChatBot")
    st.write("참조파일 : 2024 경기형 학교폭력 사안처리 매뉴얼")
    st.write(st.session_state.thread_ID_06)


if "messages_06" not in st.session_state:
    st.session_state["messages_06"] = [{"role": "assistant", "content": "안녕하세요. 학교폭력 절차에 대해 상담해 드립니다."}]

for msg in st.session_state.messages_06:
    st.chat_message(msg["role"]).write(msg["content"])
if prompt := st.chat_input():
    if not st.session_state.api_key:
       st.info("Please input your OpenAI API key to continue: at Homepage")
       st.stop()
    st.session_state.messages_06.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.beta.threads.messages.create(
    thread_id = st.session_state.thread_ID_06,
    role = "user",
    content = prompt,
    )

    run_06 = client.beta.threads.runs.create(
        thread_id = st.session_state.thread_ID_06, 
        assistant_id = assistant_ID
    )

    while True:
        run_06 = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_ID_06,
            run_id = run_06.id
        )
        if run_06.status=="completed":
            break
        else:
            time.sleep(2)
    thread_messages_06 = client.beta.threads.messages.list(st.session_state.thread_ID_06)
    msg = thread_messages_06.data[0].content[0].text.value
    print(thread_messages_06)
    st.session_state.messages_06.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
