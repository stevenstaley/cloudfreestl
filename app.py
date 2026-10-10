import streamlit as st
import os
from pathlib import Path
from styles.global_css import apply_global_css
apply_global_css(logo_height="120px")
import base64

st.logo("logocf.png", size='large', link="https://app.cloudfreestl.com")

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



pg.run()
