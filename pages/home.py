import streamlit as st
from styles.global_css import apply_global_css
apply_global_css(logo_height="120px")

container = st.container(border=True)
container.write("This is inside the container")

# show_home()