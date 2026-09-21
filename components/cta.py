import streamlit as st


def render_cta():

    st.markdown("""
    <div class="cf-cta">

        <h2>
            Let's build something better.
        </h2>

        <p>
            Tell us about your home, network, automation,
            or security project.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.button("Get Started →")
