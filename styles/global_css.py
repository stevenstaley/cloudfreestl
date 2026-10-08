import streamlit as st

def apply_global_css(logo_height="80px"):
    header_height = "150px"

    css = f"""
    <style>
    .stApp {{
        background-image: url('/app/static/background3.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    [data-testid="stMainBlockContainer"] {{
        padding-top: 10rem;
    }}

    /* =========================================================
       TOP NAVIGATION
       ========================================================= */

    [data-testid="stTopNavLink"] {{
        font-family: "Inter", sans-serif !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }}

    [data-testid="stTopNavLink"] span {{
        font-family: "Inter", sans-serif !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }}
    /* =========================================================
    Use this for the top navigation links to make them larger and more prominent
    ========================================================= */
    [data-testid="stTopNavLink"] p {{
        font-family: "Inter", sans-serif !important;
        font-size: 25px !important;
        font-weight: 500 !important;
    }}

    /* =========================================================
       HEADER
       ========================================================= */

    [data-testid="stHeader"] {{
        background-color: rgba(208, 215, 236, 0.1);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(12px);
        font-family: "Inter", sans-serif;
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

    /* =========================================================
       LOGO
       ========================================================= */

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

    /* =========================================================
       NORMAL PAGE MARKDOWN
       ========================================================= */

    .stMarkdown {{
        font-family: "Inter", sans-serif;
    }}

    </style>
    """

    st.markdown(css, unsafe_allow_html=True)