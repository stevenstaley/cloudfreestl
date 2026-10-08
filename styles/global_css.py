import streamlit as st

def apply_global_css(logo_height="80px"):
    header_height = "150px"  # logo height + padding

    css = f"""
    <style>
    .stApp {{
        background-image: url('/app/static/background.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    [data-testid="stMainBlockContainer"] {{
        padding-top: 10rem;
    }}

    [data-testid="stHeader"] {{
        background-color: rgba(208, 215, 236, 0.1);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(12px);
        font-family: 'Inter', sans-serif;
        box-shadow: none;
        height: {header_height} !important;
        min-height: {header_height} !important;
        display: flex;
        align-items: center;
    }}

    .stAppHeader span,
    .stAppHeader svg {{
        color: white !important;
    }}

    /* THIS is the critical part — override the inline max-height */
    [data-testid="stHeaderLogo"] img {{
        max-height: {logo_height} !important;
        height: {logo_height} !important;
        width: auto !important;
    }}

    [data-testid="stHeaderLogo"] {{
        height: {logo_height} !important;
        display: flex;
        align-items: center;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)   