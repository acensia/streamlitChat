import streamlit as st

def update_conversation(user_msg, bot_msg):
    st.session_state.conversation.append("You: " + user_msg)
    st.session_state.conversation.append("Bot: " + bot_msg)

def bot_start():
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []
    # Chatbot interface
    user_input = st.text_input("You: ", key=f"text{st.session_state.cnt}")
    if user_input:
        # Process user_input and generate bot_response
        bot_response = "This is a response from the bot."
        update_conversation(user_input, bot_response)

        st.session_state.cnt += 1
        st.session_state[f"text{st.session_state.cnt}"] = ""
        st.rerun()

    for msg in st.session_state.conversation:
        st.text(msg)