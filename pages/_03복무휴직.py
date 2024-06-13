from openai import OpenAI
import streamlit as st
import time

client = OpenAI(api_key = st.session_state.api_key)
assistant_ID = "asst_QygWriWg8cvHmXwaSSJlWUUi"


if "thread_ID_03" not in st.session_state:
    thread_03 = client.beta.threads.create()
    st.session_state.thread_ID_03 = thread_03.id

with st.sidebar:
    st.title("💬 복무와 휴복직 ChatBot")
    st.write("참조파일 : 23 인사실무편람")
    st.write(st.session_state.thread_ID_03)


if "messages_03" not in st.session_state:
    st.session_state["messages_03"] = [{"role": "assistant", "content": "안녕하세요. 교원의 복무 및 휴복직에 대해 물어보세요?"}]

for msg in st.session_state.messages_03:
    st.chat_message(msg["role"]).write(msg["content"])
if prompt := st.chat_input():
   if not st.session_state.api_key:
       st.info("Please input your OpenAI API key to continue: at Homepage")
       st.stop()
   st.session_state.messages_03.append({"role": "user", "content": prompt})
   st.chat_message("user").write(prompt)

   response = client.beta.threads.messages.create(
   thread_id = st.session_state.thread_ID_03,
   role = "user",
   content = prompt,
   )

run_03 = client.beta.threads.runs.create(
    thread_id = st.session_state.thread_ID_03, 
    assistant_id = assistant_ID
   )

while True:
    run_03 = client.beta.threads.runs.retrieve(
        thread_id=st.session_state.thread_ID_03,
        run_id = run_03.id
    )
    if run_03.status=="completed":
        break
    else:
        time.sleep(2)
thread_messages_03 = client.beta.threads.messages.list(st.session_state.thread_ID_03)
msg = thread_messages_03.data[0].content[0].text.value
print(thread_messages_03)
st.session_state.messages_03.append({"role": "assistant", "content": msg})
st.chat_message("assistant").write(msg)
