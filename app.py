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
    # st.Page("/pages/examples.py", title="Examples"),
    # st.Page("/pages/community.py", title="Community"),
]

pg = st.navigation(
    pages,
    position="top",
)

pg.run()
