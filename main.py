import streamlit as st

st.set_page_config(page_title="Poetry House 🌸", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff0f5;
    }
    h1 {
        color: #6a0dad;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    .welcome-box {
        background-color: #ffe4e1;
        padding: 20px;
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>🌸 Welcome to the Poetry House</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div class='welcome-box'>
    Step in. Breathe. 🌿<br><br>
    This is a safe space for your feelings and thoughts.<br><br>
    Explore poems, find comfort, or share your mood.
    </div>
    """,
    unsafe_allow_html=True
)

st.info("👉 Click 'Poetry Page' from the sidebar to enter 🌷")
