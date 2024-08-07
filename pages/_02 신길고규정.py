from openai import OpenAI
import streamlit as st
import time

client = OpenAI(api_key = st.session_state.api_key)
assistant_ID = "asst_agxPLU5ACDAPPAmSghHZ7FyL"


if "thread_ID_02" not in st.session_state:
    thread_02 = client.beta.threads.create()
    st.session_state.thread_ID_02 = thread_02.id

with st.sidebar:
    st.title("💬 신길고등학교 규정 ChatBot")
    st.write("참조파일 : 2024 신길고등학교 규정집 ")
    st.write(st.session_state.thread_ID_02)


if "messages_02" not in st.session_state:
    st.session_state["messages_02"] = [{"role": "assistant", "content": "안녕하세요. 신길고 규정에 대해 궁금하신점을 물어보세요.?"}]

for msg in st.session_state.messages_02:
    st.chat_message(msg["role"]).write(msg["content"])
if prompt := st.chat_input():
    if not st.session_state.api_key:
       st.info("Please input your OpenAI API key to continue: at Homepage")
       st.stop()
    st.session_state.messages_02.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.beta.threads.messages.create(
    thread_id = st.session_state.thread_ID_02,
    role = "user",
    content = prompt,
    )

    run_02 = client.beta.threads.runs.create(
        thread_id = st.session_state.thread_ID_02, 
        assistant_id = assistant_ID
    )

    while True:
        run_02 = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_ID_02,
            run_id = run_02.id
        )
        if run_02.status=="completed":
            break
        else:
            time.sleep(2)
    thread_messages_02 = client.beta.threads.messages.list(st.session_state.thread_ID_02)
    msg = thread_messages_02.data[0].content[0].text.value
    print(thread_messages_02)
    st.session_state.messages_02.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
