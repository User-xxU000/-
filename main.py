import streamlit as st

st.set_page_config(page_title="Незаконные вещи 😈")

if "messages" not in st.session_state:
    st.session_state.messages = []

#st.write(st.session_state.messages)
for messages in st.session_state.messages:
    with st.chat_message(messages.get("role")):
        st.write(messages.get("content"))


promnt = st.chat_input("Say Something!")



if promnt:
    #added to storage
    st.session_state.messages.append({"role":"user","content":promnt})
    with st.chat_message("user",avatar="😈"):
        st.write(promnt)
