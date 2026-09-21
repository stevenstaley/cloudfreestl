import streamlit as st


def render_header():

    st.markdown("""
    <div class="cf-header">

        <div class="cf-logo">

            <div class="cf-logo-icon">
                ☁
            </div>

            <div>
                CloudFree STL

                <span class="cf-logo-subtitle">
                    Private · Local · Yours
                </span>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)
