import streamlit as st
import streamlit_authenticator as stauth

def st_auth():
    if st.session_state.starts == "out":
        if st.button("Wanna start?"):
            st.session_state.starts = "in"
            st.rerun()
    else:
        if st.button("Wanna out?"):
            st.session_state.starts = "out"
            st.session_state.conversation = []
            st.rerun()

"""
def st_auth():
# Create a list of usernames, names, and hashed passwords
    users = ["user1", "user2"]
    names = ["Name1", "Name2"]
    hashed_passwords = stauth.Hasher(["password1", "password2"]).generate()

    # Create an authentication object
    authenticator = stauth.Authenticate(
        users,
        names,
        hashed_passwords,
        "some_cookie_name",
        "some_signature_key",
        cookie_expiry_days=30)

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status:
        st.write(f"Welcome *{name}*")
        # Chatbot functionality goes here
    elif authentication_status == False:
        st.error("Username/password is incorrect")
    elif authentication_status == None:
        st.warning("Please enter your username and password")
"""