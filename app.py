import streamlit as st
from pathlib import Path

from components.header import render_header
from components.hero import render_hero
from components.trust import render_trust
from components.services import render_services
from components.cta import render_cta
from components.footer import render_footer


st.set_page_config(
    page_title="CloudFree STL",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)




CSS_FILE = Path(__file__).parent / "styles" / "main.css"
with open(CSS_FILE, "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# Page
render_header()

render_hero()

render_trust()

render_services()

render_cta()

render_footer()
