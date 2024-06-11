from openai import OpenAI
import streamlit as st
    
# st.title("💬 학교생활기록부챗봇")
# st.caption("🚀 A Streamlit chatbot powered by OpenAI")
OpenAI_API_Key = st.secrets["API_KEY"]
client = OpenAI(api_key=OpenAI_API_Key)

def assistantsID(chatbotName):
    my_assistants = client.beta.assistants.list(
    order="desc",
    limit="20",
    )
    count = my_assistants.data.count('Assistant')
    x=0
    isFind = False
    while x <= count:
        if my_assistants.data[x].name == chatbotName:
            return my_assistants.data[x].id

assistant_ID = assistantsID('학교생활기록부챗봇')
st.wirte(assistant_ID)

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
