import streamlit as st


def render_hero():
    st.markdown("""
    <div class="cf-hero">

        <div class="cf-eyebrow">
            Local Technology · Real Privacy · St. Louis
        </div>

        <h1>
            Technology Solutions
            <span class="cf-hero-highlight">
                Without the Cloud.
            </span>
        </h1>

        <p class="cf-hero-text">
            Smart home automation, security, and networking
            solutions designed around your home, your privacy,
            and your control.
        </p>

    </div>
    """, unsafe_allow_html=True)
