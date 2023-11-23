import streamlit as st
from auth import st_auth
from bot import bot_start
from state_man import init_state



def front():
    init_state()
    st.title("Chatbot Web App")
    st_auth()
    if st.session_state.starts == "in":
        bot_start()


if __name__ == "__main__":
    front()



