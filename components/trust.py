import streamlit as st


def render_trust():

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="cf-feature">
            <div class="cf-feature-icon">🔒</div>
            <h3>Your Privacy</h3>
            <p>
                Your data stays under your control.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cf-feature">
            <div class="cf-feature-icon">📍</div>
            <h3>Local Expertise</h3>
            <p>
                Technology solutions built for St. Louis.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="cf-feature">
            <div class="cf-feature-icon">☁️</div>
            <h3>No Unnecessary Cloud</h3>
            <p>
                Own your technology instead of renting it.
            </p>
        </div>
        """, unsafe_allow_html=True)
