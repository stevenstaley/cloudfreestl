import streamlit as st
import os
from pathlib import Path
# from utils.functions import set_bg_hack
from styles.global_css import apply_global_css
import base64

apply_global_css()

st.set_page_config(
    page_title="Cloud Free STL",
    layout="wide",
)
 

pages = [
    st.Page("pages/home.py", title="Home"),
    st.Page("pages/services.py", title="Services"),
    st.Page("pages/about.py", title="About"),
]

pg = st.navigation(
    pages,
    position="top",
)
st.logo("logo-transparent.png", size='large', link="https://app.cloudfreestl.com")


pg.run()
