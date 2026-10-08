import streamlit as st
from styles.global_css import apply_global_css


# def show_home():
st.image("businesscard-transparent.png", caption="test", width=750)
container = st.container(border=True)
container.write("This is inside the container")
apply_global_css()
# show_home()