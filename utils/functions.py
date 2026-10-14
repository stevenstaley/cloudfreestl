import streamlit as st
import base64
from pathlib import Path
import requests
import re

def set_bg_hack(local_image_path):
    # Read and encode the image
    with open(local_image_path, "rb") as f:
        img_data = f.read()
    base64_img = base64.b64encode(img_data).decode()
    
    # Determine extension
    ext = local_image_path.split('.')[-1]
    
    # Apply CSS
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/{ext};base64,{base64_img}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



from pathlib import Path
import base64

def load_png_icon(filename, size=28):
    # Go up from utils/ to the project root, then into static/
    icon_path = Path(__file__).resolve().parent.parent / "static" / filename

    with open(icon_path, "rb") as icon_file:
        encoded = base64.b64encode(icon_file.read()).decode("utf-8")

    return f"""
        <img
            src="data:image/png;base64,{encoded}"
            width="{size}"
            height="{size}"
            style="object-fit:contain; vertical-align:middle;"
        />
    """

@st.dialog("Contact Form", position="center", width="large")
def show_contact_form():
    st.write("Please fill out the form below:")

    with st.form("contact_form"):
        name = st.text_input("Name", max_chars=100)
        email = st.text_input("Email", max_chars=254)
        message = st.text_area("Message", max_chars=5000)

        submitted = st.form_submit_button(
            "Send Message",
            use_container_width=True,
        )

    if submitted:
        name = name.strip()
        email = email.strip()
        message = message.strip()

        if not name or not email or not message:
            st.error("Please complete all fields.")
            return

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            st.error("Please enter a valid email address.")
            return

        try:
            response = requests.post(
                st.secrets["CONTACT_WEBHOOK_URL"],
                json={
                    "name": name,
                    "email": email,
                    "message": message,
                },
                timeout=15,
            )
            response.raise_for_status()

            st.success(
                "Thank you! Your message has been received."
            )

        except requests.RequestException:
            st.error(
                "We couldn't submit your message right now. "
                "Please try again later."
            )


# with st.container(key="contact-panel"):
#     st.markdown("### Ready to Talk?")
#     st.write(
#         "We'd love to hear about your project "
#         "and help you find the right solution."
#     )

#     if st.button("Contact Us", use_container_width=True):
#         show_contact_form()