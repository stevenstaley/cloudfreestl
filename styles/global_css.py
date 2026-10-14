import streamlit as st

def apply_global_css(logo_height="80px"):
    header_height = "150px"

    css = f"""
    <style>

    /* =========================================================
       GLOBAL APP BACKGROUND
       ========================================================= */
    .stApp {{
    background-image: linear-gradient(rgba(4, 15, 30, 0.42), rgba(4, 15, 30, 0.55)), url('/app/static/background3.png');
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
        color: #ffffff !important;
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
       CUSTOM BUTTON STYLES
       ========================================================= */
    div.stButton > button,
    div.stLinkButton > a {{
        background: linear-gradient(135deg, #ff9b59 0%, #ff6a00 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.8rem 1.45rem !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.02em !important;
        box-shadow: 0 10px 20px rgba(255, 106, 0, 0.24) !important;
        transition: transform 0.15s ease, box-shadow 0.15s ease, filter 0.15s ease !important;
        text-decoration: none !important;
        width: fit-content !important;
        min-width: 180px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}

    div.stButton > button:hover,
    div.stLinkButton > a:hover {{
        background: linear-gradient(135deg, #ffb06d 0%, #ff7a1a 100%) !important;
        box-shadow: 0 12px 22px rgba(255, 122, 26, 0.32) !important;
        transform: translateY(-1px) !important;
        filter: brightness(1.03) !important;
    }}

    div.stButton > button:focus,
    div.stLinkButton > a:focus {{
        outline: 2px solid rgba(255, 160, 91, 0.8) !important;
        outline-offset: 2px !important;
        box-shadow: 0 0 0 4px rgba(255, 122, 26, 0.18) !important;
    }}

    div.stLinkButton > a {{
        line-height: 1.2 !important;
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



def apply_services_css():
    st.markdown(
        """
        <style>
        /* =====================================
           GLOBAL SECTION STYLING
        ===================================== */

        .st-key-feature-row,
        .st-key-services-layout {
            color: #f4eeee;
        }

        .st-key-feature-row {
            padding: 8px 8px 22px 8px;
            margin-bottom: 8px;
        }

        /* =====================================
           TOP FEATURE ROW
        ===================================== */

        .st-key-feature-row [data-testid="stHorizontalBlock"] {
            gap: 22px;
        }

        .st-key-feature-row [data-testid="column"] {
            padding: 8px 14px;
            border-right: 1px solid rgba(238, 116, 62, 0.15);
        }

        .st-key-feature-row [data-testid="column"]:last-child {
            border-right: none;
        }

        .st-key-feature-row h3 {
            color: #f5eeee;
            font-size: 18px;
            font-weight: 650;
            margin-bottom: 4px;
        }

        .st-key-feature-row [data-testid="stCaptionContainer"] {
            color: #ffffff;
            font-size: 14px;
        }

        /* =====================================
           MAIN TWO-COLUMN LAYOUT
        ===================================== */

        .st-key-services-layout [data-testid="stHorizontalBlock"] {
            align-items: stretch;
            gap: 16px;
        }

        /* =====================================
           SERVICES PANEL
        ===================================== */

        .st-key-services-panel {
            height: 100%;
            background: linear-gradient(
                135deg,
                rgba(87, 49, 42, 0.48),
                rgba(32, 31, 38, 0.96)
            );
            border: 1px solid rgba(225, 111, 63, 0.17);
            border-radius: 22px;
            padding: 20px 20px 18px 20px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }

        .st-key-services-panel h2 {
            color: #f4eeee;
            font-size: 18px;
            font-weight: 700;
            letter-spacing: 0.4px;
            margin-bottom: 14px;
        }

        /* Four service cards */

        .st-key-services-panel [data-testid="stHorizontalBlock"] {
            gap: 14px;
        }

        .st-key-service-home,
        .st-key-service-security,
        .st-key-service-networking,
        .st-key-service-consulting {
            min-height: 168px;
            height: 100%;
            padding: 16px 14px;
            background: linear-gradient(
                145deg,
                rgba(101, 57, 47, 0.62),
                rgba(75, 49, 47, 0.76)
            );
            border: 1px solid rgba(237, 125, 72, 0.13);
            border-radius: 18px;
            transition: all 0.2s ease;
        }

        .st-key-service-home:hover,
        .st-key-service-security:hover,
        .st-key-service-networking:hover,
        .st-key-service-consulting:hover {
            border-color: rgba(255, 133, 72, 0.65);
            transform: translateY(-3px);
            background: rgba(111, 61, 48, 0.8);
        }

        .st-key-services-panel h3 {
            color: #f5eeee;
            font-size: 16px;
            line-height: 1.3;
            margin-top: 4px;
            margin-bottom: 6px;
        }

        .st-key-services-panel [data-testid="stMarkdownContainer"] p {
            color: #c1b4b3;
            font-size: 13px;
            line-height: 1.5;
        }

        .st-key-services-panel [data-testid="stMarkdownContainer"] h2 {
            color: #ff8b49;
            font-size: 30px;
            margin-bottom: 10px;
        }

        /* =====================================
           CONTACT PANEL
        ===================================== */

        .st-key-contact-panel {
            height: 100%;
            min-height: 260px;
            padding: 24px 24px 22px 24px;
            background: linear-gradient(
                145deg,
                #9b482e 0%,
                #743b36 58%,
                #63363a 100%
            );
            border: 1px solid rgba(255, 139, 73, 0.9);
            border-radius: 19px;
            box-shadow:
                inset 0 1px 0 rgba(255, 205, 164, 0.13),
                0 6px 22px rgba(0, 0, 0, 0.16);
        }

        .st-key-contact-panel h3 {
            color: #fff4ed;
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .st-key-contact-panel p {
            color: #f0d1c8;
            font-size: 15px;
            line-height: 1.65;
        }

        .st-key-contact-panel .stButton button {
            background: linear-gradient(
                135deg,
                #ff8244,
                #f36c35
            );
            color: #ffffff;
            border: 1px solid rgba(255, 188, 140, 0.45);
            border-radius: 12px;
            min-height: 48px;
            font-size: 15px;
            font-weight: 650;
            transition: all 0.2s ease;
        }

        .st-key-contact-panel .stButton button:hover {
            background: #ff945e;
            border-color: #ffbd98;
            color: #ffffff;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        }

        /* =====================================
           RESPONSIVE SPACING
        ===================================== */

        @media (max-width: 900px) {
            .st-key-feature-row {
                padding: 4px;
            }

            .st-key-services-panel,
            .st-key-contact-panel {
                padding: 16px;
            }
        }


        /* =====================================
        REFINEMENTS — MATCH REFERENCE IMAGE
        ===================================== */

        /* Keep the background from overpowering the panels */
        .stApp {
            background-color: #1e1d24;
        }

        .st-key-feature-row,
        .st-key-services-layout {
            color: #f3eded;
        }

        /* Top feature row */
        .st-key-feature-row {
            padding: 4px 12px 12px 12px;
            margin-bottom: 2px;
        }

        .st-key-feature-row [data-testid="stHorizontalBlock"] {
            gap: 14px;
        }

        .st-key-feature-row [data-testid="column"] {
            padding: 8px 12px;
        }

        .st-key-feature-row h3 {
            font-size: 16px;
            line-height: 1.35;
            margin: 0 0 5px 0;
        }

        .st-key-feature-row [data-testid="stCaptionContainer"] {
            font-size: 13px;
        }

        /* Reduce the divider's visual weight */
        .st-key-feature-row + div {
            margin-top: 0;
        }

        /* Main services panel */
        .st-key-services-panel {
            padding: 16px 18px 18px 18px;
            border-radius: 20px;
            background: rgba(34, 31, 37, 0.94);
            border-color: rgba(223, 116, 69, 0.18);
        }

        .st-key-services-panel h2 {
            font-size: 17px;
            margin-bottom: 12px;
        }

        /* Make four cards fit evenly */
        .st-key-services-panel [data-testid="stHorizontalBlock"] {
            gap: 10px;
        }

        .st-key-service-home,
        .st-key-service-security,
        .st-key-service-networking,
        .st-key-service-consulting {
            min-width: 0;
            min-height: 155px;
            padding: 13px 12px;
            border-radius: 16px;
            background: rgba(91, 56, 49, 0.68);
            border-color: rgba(225, 120, 74, 0.16);
        }

        /* Smaller icons */
        .st-key-services-panel [data-testid="stMarkdownContainer"] h2 {
            font-size: 27px;
            line-height: 1.2;
            margin: 0 0 10px 0;
        }

        /* Service titles */
        .st-key-services-panel h3 {
            font-size: 14px;
            line-height: 1.3;
            margin: 0 0 7px 0;
            overflow-wrap: normal;
            word-break: normal;
        }

        /* Descriptions */
        .st-key-services-panel [data-testid="stMarkdownContainer"] p {
            font-size: 12px;
            line-height: 1.45;
            margin-bottom: 0;
        }

        /* Contact panel: less tall, closer to reference */
        .st-key-contact-panel {
            min-height: 0;
            padding: 22px 22px;
            border-radius: 17px;
            background: linear-gradient(
                145deg,
                rgba(143, 65, 44, 0.97),
                rgba(91, 48, 49, 0.98)
            );
        }

        .st-key-contact-panel h3 {
            font-size: 19px;
            margin-bottom: 10px;
        }

        .st-key-contact-panel p {
            font-size: 13px;
            line-height: 1.6;
        }

        /* Button */
        .st-key-contact-panel .stButton button {
            width: auto;
            min-width: 145px;
            min-height: 43px;
            padding: 0 20px;
            border-radius: 10px;
            font-size: 13px;
        }

        /* Reduce excess vertical space */
        .st-key-services-layout {
            margin-top: 0;
        }

        @media (max-width: 900px) {
            .st-key-services-panel {
                padding: 14px;
            }

            .st-key-service-home,
            .st-key-service-security,
            .st-key-service-networking,
            .st-key-service-consulting {
                padding: 10px;
            }

            .st-key-services-panel h3 {
                font-size: 12px;
            }
        }

                
        /* Hide anchor links beside headings */
        .stApp [data-testid="stHeaderActionElements"],
        .stApp [data-testid="stMarkdownHeaderLink"],
        .stApp .stMarkdown a.header-anchor {
            display: none !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
