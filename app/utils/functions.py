import streamlit as st
import base64

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

# Usage: set_bg_hack('background.png')   