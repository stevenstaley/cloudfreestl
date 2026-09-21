import streamlit as st


def render_services():

    st.markdown("""
    <div class="cf-section-label">
        OUR SERVICES
    </div>

    <h2 class="cf-section-title">
        Technology built around you.
    </h2>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="cf-service">
            <div class="cf-service-icon">🏠</div>
            <h3>Home Automation</h3>
            <p>
                Smart, comfortable homes without depending
                on unnecessary cloud services.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cf-service">
            <div class="cf-service-icon">🛡️</div>
            <h3>Security</h3>
            <p>
                Protect your home and devices with
                locally controlled security systems.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="cf-service">
            <div class="cf-service-icon">🌐</div>
            <h3>Networking</h3>
            <p>
                Fast, reliable networks designed around
                your home and your needs.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="cf-service">
            <div class="cf-service-icon">⚙️</div>
            <h3>Consulting</h3>
            <p>
                Expert guidance for building a
                private, reliable technology environment.
            </p>
        </div>
        """, unsafe_allow_html=True)
