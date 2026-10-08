import streamlit as st
import os
from pathlib import Path
import base64

st.set_page_config(
    page_title="Cloud Free STL",
    layout="wide",
)

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("assets/background.png");
  background-size: cover;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)

pages = [
    st.Page("pages/home.py", title="Home"),
    st.Page("pages/services.py", title="Services"),
    st.Page("pages/about.py", title="About"),
    # st.Page("pages/examples.py", title="Examples"),
    # st.Page("pages/community.py", title="Community"),
]

pg = st.navigation(
    pages,
    position="top",
)

pg.run()
