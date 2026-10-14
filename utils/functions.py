import streamlit as st
import base64
from pathlib import Path

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

