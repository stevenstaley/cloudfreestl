import streamlit as st

def apply_global_css(logo_height="80px"):
    header_height = "150px"

    css = f"""
    <style>

    /* =========================================================
       GLOBAL APP BACKGROUND
       ========================================================= */
    .stApp {{
        background-image: url('/app/static/background3.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* =========================================================
       MAIN CONTENT SPACING
       ========================================================= */
    [data-testid="stMainBlockContainer"] {{
        padding-top: 9rem;
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
       TEXT / MARKDOWN BASE STYLES
       ========================================================= */
    .stMarkdown {{
        font-family: "Inter", sans-serif;
    }}

    /* =========================================================
       MARKDOWN HEADINGS
       ========================================================= */

    [data-testid="stMarkdownContainer"] h1 {{
        font-family: "Inter", sans-serif !important;
        font-size: 50px !important;
        font-weight: 600 !important;
        font-style: normal !important;
        color: #ffffff !important;
        opacity: 1 !important;
        line-height: 1.2 !important;
        letter-spacing: 0px !important;
        word-spacing: 0px !important;
        margin-top: 0px !important;
        margin-bottom: 16px !important;
        text-align: left !important;
        text-transform: none !important;
        text-decoration: none !important;
        text-shadow: none !important;
        overflow-wrap: break-word !important;
    }}

    [data-testid="stMarkdownContainer"] h2 {{
        font-family: "Inter", sans-serif !important;
        font-size: 40px !important;
        font-weight: 600 !important;
        font-style: normal !important;
        color: #ffffff !important;
        opacity: 1 !important;
        line-height: 1.3 !important;
        letter-spacing: 0px !important;
        word-spacing: 0px !important;
        margin-top: 0px !important;
        margin-bottom: 5px !important;
        text-align: left !important;
        text-transform: none !important;
        text-decoration: none !important;
        text-shadow: none !important;
        overflow-wrap: break-word !important;
    }}

    [data-testid="stMarkdownContainer"] h3 {{
        font-family: "Inter", sans-serif !important;
        font-size: 32px !important;
        font-weight: 600 !important;
        font-style: normal !important;
        color: #ffffff !important;
        opacity: 1 !important;
        line-height: 1.4 !important;
        letter-spacing: 0px !important;
        word-spacing: 0px !important;
        margin-top: 0px !important;
        margin-bottom: 5px !important;
        text-align: left !important;
        text-transform: none !important;
        text-decoration: none !important;
        text-shadow: none !important;
        overflow-wrap: break-word !important;
    }}

    [data-testid="stMarkdownContainer"] h4 {{
        font-family: "Inter", sans-serif !important;
        font-size: 25px !important;
        font-weight: 600 !important;
        font-style: normal !important;
        color: #ff0000 !important;
        opacity: 1 !important;
        line-height: 1.2 !important;
        letter-spacing: 0px !important;
        word-spacing: 0px !important;
        margin-top: 0px !important;
        margin-bottom: 5px !important;
        text-align: left !important;
        text-transform: none !important;
        text-decoration: none !important;
        text-shadow: none !important;
        overflow-wrap: break-word !important;
    }}

    [data-testid="stMarkdownContainer"] h4 *,
    [data-testid="stMarkdownContainer"] h4 span {{
        font-family: "Inter", sans-serif !important;
        font-size: 20px !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }}

    [data-testid="stMarkdownContainer"] h5 {{
        font-family: "Inter", sans-serif !important;
        font-size: 22px !important;
        font-weight: 500 !important;
        font-style: normal !important;
        color: #e2e8f0 !important;
        opacity: 1 !important;
        line-height: 1 !important;
        letter-spacing: 0px !important;
        word-spacing: 0px !important;
        margin-top: 0px !important;
        margin-bottom: 10px !important;
        text-align: left !important;
        text-transform: none !important;
        text-decoration: none !important;
        text-shadow: none !important;
        overflow-wrap: break-word !important;
    }}

    [data-testid="stMarkdownContainer"] h6 {{
        font-family: "Inter", sans-serif !important;
        font-size: 18px !important;
        font-weight: 500 !important;
        font-style: normal !important;
        color: #cbd5e1 !important;
        opacity: 1 !important;
        line-height: 1.5 !important;
        letter-spacing: 0px !important;
        word-spacing: 0px !important;
        margin-top: 0px !important;
        margin-bottom: 8px !important;
        text-align: left !important;
        text-transform: none !important;
        text-decoration: none !important;
        text-shadow: none !important;
        overflow-wrap: break-word !important;
    }}

    /* =========================================================
       MOBILE RESPONSIVE STYLES
       ========================================================= */
    @media (max-width: 768px) {{
        [data-testid="stMainBlockContainer"] {{
            padding-top: 6rem;
        }}

        [data-testid="stHeader"] {{
            height: auto !important;
            min-height: 80px !important;
            padding: 0.5rem 0.75rem !important;
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.25rem;
        }}

        [data-testid="stHeaderLogo"] {{
            height: 52px !important;
            margin-right: auto;
        }}

        [data-testid="stHeaderLogo"] img {{
            max-height: 52px !important;
            height: 52px !important;
        }}

        [data-testid="stTopNavLink"] {{
            font-size: 13px !important;
            padding: 0.35rem 0.5rem !important;
            white-space: nowrap;
        }}

        [data-testid="stTopNavLink"] span,
        [data-testid="stTopNavLink"] p {{
            font-size: 13px !important;
            line-height: 1.2 !important;
        }}
    }}

    @media (max-width: 480px) {{
        [data-testid="stHeader"] {{
            min-height: 72px !important;
            padding: 0.35rem 0.5rem !important;
        }}

        [data-testid="stHeaderLogo"] img {{
            max-height: 42px !important;
            height: 42px !important;
        }}

        [data-testid="stTopNavLink"] {{
            font-size: 12px !important;
            padding: 0.25rem 0.4rem !important;
        }}

        [data-testid="stMarkdownContainer"] h1 {{
            font-size: 32px !important;
        }}

        [data-testid="stMarkdownContainer"] h2 {{
            font-size: 28px !important;
        }}

        [data-testid="stMarkdownContainer"] h3 {{
            font-size: 24px !important;
        }}
    }}

    </style>
    """

    st.markdown(css, unsafe_allow_html=True)