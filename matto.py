import streamlit as st
import os
import random

BASE_PATH = r"G:\My Drive\manufacturing_datasets"

st.title("Manufacturing Defect Image Viewer")

# Dropdowns
process = st.selectbox("Select Process", ["welding", "casting", "machining"])
defect = st.selectbox("Select Defect Type", ["crack", "rust", "porosity"])

# Button
if st.button("Generate Image"):

    folder_path = os.path.join(BASE_PATH, process, defect) 

    st.write("Folder Used:", folder_path)

    if os.path.exists(folder_path):

        image_files = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
        ]

        if image_files:

            selected_image = random.choice(image_files)

            image_path = os.path.join(folder_path, selected_image)

            st.image(image_path, caption=selected_image, use_container_width=True)

        else:
            st.warning("No images found inside crack folder.")

    else:
        st.error("Folder path not found.")