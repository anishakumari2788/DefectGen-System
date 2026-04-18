import streamlit as st
from PIL import Image
import numpy as np

# ---- Dummy model function (replace with your real model) ----
def generate_image(process, material, defect):
    # For now, create a placeholder image
    img = np.zeros((256, 256, 3), dtype=np.uint8)
    
    if defect == "Crack":
        img[:, :] = [255, 0, 0]  # red
    elif defect == "Hole":
        img[:, :] = [0, 255, 0]  # green
    else:
        img[:, :] = [0, 0, 255]  # blue
    
    return Image.fromarray(img)

# ---- UI ----
st.set_page_config(page_title="Defect Generator", layout="centered")

st.title("🛠️ Defect Image Generator")

st.markdown("Generate defect images based on manufacturing parameters")

# ---- Inputs ----
process = st.selectbox(
    "Select Process",
    ["Casting", "Welding", "Machining"]
)

material = st.selectbox(
    "Select Material",
    ["Steel", "Aluminum", "Plastic"]
)

defect = st.selectbox(
    "Select Defect Type",
    ["Crack", "Hole", "Scratch"]
)

# ---- Button ----
if st.button("Generate Image"):
    with st.spinner("Generating..."):
        image = generate_image(process, material, defect)
        
        st.success("Done!")
        st.image(image, caption=f"{process} | {material} | {defect}", use_container_width=True)