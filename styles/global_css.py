import streamlit as st

def apply_global_css():
    css = """
    <style>
    .stApp {
        background-image: url('/app/static/background.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    [data-testid="stHeader"] {
        background-color: rgba(255, 255, 255, 0.5);
        box-shadow: none;
    }

    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0);
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)   