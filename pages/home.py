import streamlit as st
from styles.global_css import apply_global_css, apply_services_css
# from utils.functions import load_png_icon
apply_global_css(logo_height="120px")
apply_services_css()


with st.container():
    st.markdown(
        """
        # Your Technology. Your Data. <span style=\"color: #ff7a1a;\">Your Rules.</span>

        ###### Every home and business has different needs. We work with you to understand your goals, recommend the right technology, and build customized solutions that prioritize privacy, reliability, and local control—without depending on cloud services.
        """,
        unsafe_allow_html=True,
    )

if st.button("Explore Services ->"):
    st.switch_page("pages/services.py")   

with st.container(key="feature-row"):
    features = st.columns(3, gap="small")

    with features[0]:
        st.markdown("### 🛡️ Privacy Focused")
        st.caption("#### Your data. Your control.")

    with features[1]:
        st.markdown("### 📍 Local Team")
        st.caption("#### Based in St. Louis.")

    with features[2]:
        st.markdown("### ☁️ No Cloud Required")
        st.caption("#### Simple. Reliable. Yours.")

# st.divider()

# --------------------------------------------------
# SERVICES + CONTACT SECTION
# --------------------------------------------------

with st.container(key="services-layout"):
    services_column, contact_column = st.columns(
        [3.3, 1.25],
        gap="medium"
    )

    with services_column:
        with st.container(key="services-panel"):
            st.subheader("Our Services")

            service_columns = st.columns(3, gap="small")

            with service_columns[0]:
                with st.container(key="service-home"):
                    st.markdown("## 🏠")
                    st.markdown("### Home Automation")
                    st.caption("Make life easier.")

            # with service_columns[1]:
            #     with st.container(key="service-security"):
            #         st.markdown("## 🛡️")
            #         st.markdown("### Security")
            #         st.caption("Peace of mind.")

            with service_columns[1]:
                with st.container(key="service-networking"):
                    st.markdown("## ⚙️")
                    st.markdown("### Networking")
                    st.caption("Stay connected.")

            with service_columns[2]:
                with st.container(key="service-consulting"):
                    st.markdown("## 👤")
                    st.markdown("### Consulting")
                    st.caption("Get expert advice.")

    with contact_column:
        with st.container(key="contact-panel"):
            st.markdown("### Ready to Talk?")
            st.write(
                "We'd love to hear about your project "
                "and help you find the right solution."
            )

            if st.button(
                "Contact Us  →",
                key="services_contact",
                use_container_width=True
            ):
                st.session_state["show_contact_form"] = True


