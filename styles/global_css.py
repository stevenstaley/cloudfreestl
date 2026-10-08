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

    # [data-testid="stHeader"] {
    #     background-color: rgba(255, 255, 255, 0.5);
    #     box-shadow: none;
    #     color: white;
    # }

    # [data-testid="stSidebar"] {
    #     background-color: rgba(0, 0, 0, 0);
    # }
    /* Blur + semi-transparent header */
    [data-testid="stHeader"] {
    background-color: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: none;
    color: white;
    }

    .stAppHeader span,
    .stAppHeader svg {
    color: white !important;
    }   

    /* Change the font */
    [data-testid="stHeader"] {
    font-family: 'Inter', sans-serif;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)   