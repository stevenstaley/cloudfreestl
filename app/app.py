import streamlit as st
import os
from pathlib import Path
# from utils.functions import set_bg_hack
from styles.global_css import apply_global_css
import base64

apply_global_css()

st.set_page_config(
    page_title="Cloud Free STL",
    layout="wide",
)

# def set_bg_hack(local_image_path):
#     # Read and encode the image
#     with open(local_image_path, "rb") as f:
#         img_data = f.read()
#     base64_img = base64.b64encode(img_data).decode()
    
#     # Determine extension
#     ext = local_image_path.split('.')[-1]
    
#     # Apply CSS
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/{ext};base64,{base64_img}");
#             background-size: cover;
#             background-position: center;
            
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# st.markdown(
#     """
#     <style>
#     [data-testid="stHeader"] {
#         background-color: rgba(255, 255, 255, 0.3);
#         box-shadow: none;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )   

# set_bg_hack('assets/background.png') 

pages = [
    st.Page("pages/home.py", title="Home"),
    st.Page("pages/services.py", title="Services"),
    st.Page("pages/about.py", title="About"),
    # st.Page("pages/examples.py", title="Examples"),
    # st.Page("pages/community.py", title="Community"),
]

pg = st.navigation(
    pages,
    position="top",
)

pg.run()
