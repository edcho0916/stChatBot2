import streamlit as st
import datetime as dt


st.title("Welcome!! ChatBot For Teacher")

# Initialization
if 'clickNum' not in st.session_state:
    st.session_state.clickNum = 0
if 'passNum' not in st.session_state:
    st.session_state.passNum = 0

def increment_counter():
    st.session_state.clickNum += 1
    st.session_state.passNum = schPassword
# managerPass 생성
managerPass = str(465233 + dt.datetime.now().year)

# 사용자에게 학교 비밀번호를 입력받기
schPassword = st.text_input(
    "Input school password", value="", type="password", label_visibility="visible"
)
# 버튼이 클릭되었는지 확인
btn = st.button('submit', type="secondary",  on_click=increment_counter)

# 버튼이 클릭되고 입력된 비밀번호가 관리자 비밀번호와 일치하는지 확인
if btn:
    if schPassword == managerPass:
        st.write('It''s Ok, Wait a moment!!')
        st.session_state.clickNum = 0
    else:
        if st.session_state.clickNum < 3 :
            st.write('Incorrect password!!!, Input correct password')
        else:
            st.text('Incorrect password!! IF you forgot, contact me by GOE messager : 신길고 조중현')


