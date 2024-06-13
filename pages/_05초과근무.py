from openai import OpenAI
import streamlit as st
import time

client = OpenAI(api_key = st.session_state.api_key)
assistant_ID = "asst_EV53G9Tpf8ElzNnGjKrkFNZQ"


if "thread_ID_05" not in st.session_state:
    thread_05 = client.beta.threads.create()
    st.session_state.thread_ID_05 = thread_05.id

with st.sidebar:
    st.title("💬 초과근무 ChatBot")
    st.write("참조파일 : E-dasan 초과근무 FAQ 모음집")
    st.write(st.session_state.thread_ID_05)


if "messages_05" not in st.session_state:
    st.session_state["messages_05"] = [{"role": "assistant", "content": "안녕하세요. 초과근무에 대해 상담해 드립니다."}]

for msg in st.session_state.messages_05:
    st.chat_message(msg["role"]).write(msg["content"])
if prompt := st.chat_input():
   if not st.session_state.api_key:
       st.info("Please input your OpenAI API key to continue: at Homepage")
       st.stop()
   st.session_state.messages_05.append({"role": "user", "content": prompt})
   st.chat_message("user").write(prompt)

   response = client.beta.threads.messages.create(
   thread_id = st.session_state.thread_ID_05,
   role = "user",
   content = prompt,
   )

run_05 = client.beta.threads.runs.create(
    thread_id = st.session_state.thread_ID_05, 
    assistant_id = assistant_ID
   )

while True:
    run_05 = client.beta.threads.runs.retrieve(
        thread_id=st.session_state.thread_ID_05,
        run_id = run_05.id
    )
    if run_05.status=="completed":
        break
    else:
        time.sleep(2)
thread_messages_05 = client.beta.threads.messages.list(st.session_state.thread_ID_05)
msg = thread_messages_05.data[0].content[0].text.value
print(thread_messages_05)
st.session_state.messages_05.append({"role": "assistant", "content": msg})
st.chat_message("assistant").write(msg)
