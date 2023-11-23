import streamlit as st

def init_state():
    if "starts" not in st.session_state:
        st.session_state.starts = "out"
    
    if "cnt" not in st.session_state:
        st.session_state.cnt = 0