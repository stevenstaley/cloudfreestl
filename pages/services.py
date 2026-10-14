import streamlit as st
from styles.global_css import apply_global_css
apply_global_css(logo_height="120px")

with st.container():
    st.markdown(
        """
        # This is the services page. It is currently under construction. Please check back later for more information.

        ###### Every home and business has different needs. We work with you to understand your goals, recommend the right technology, and build customized solutions that prioritize privacy, reliability, and local control—without depending on cloud services.
        """,
        unsafe_allow_html=True,
    )