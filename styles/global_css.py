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

    /* Blur + semi-transparent header */
    [data-testid="stHeader"] {
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(1px);
        font-family: 'Inter', sans-serif;
        -webkit-backdrop-filter: blur(12px);
        box-shadow: none;
        color: white;
    }

    .stAppHeader span,
    .stAppHeader svg {
        color: white !important;
    }

     </style>
    """
    st.markdown(css, unsafe_allow_html=True)   