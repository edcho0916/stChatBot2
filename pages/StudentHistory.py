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

# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])
# if prompt := st.chat_input():
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()

#     client = OpenAI(api_key=openai_api_key)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": msg})
#     st.chat_message("assistant").write(msg)
