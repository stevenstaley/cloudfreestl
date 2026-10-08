import streamlit as st
from styles.global_css import apply_global_css


container = st.container(border=True)
container.write("This is inside the container")
apply_global_css(logo_height="120px")
# show_home()