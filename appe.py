import streamlit as st
from PIL import Image
import os
import random

# --- NEW IMPORTS FOR SSIM ---
from skimage.metrics import structural_similarity as ssim
import numpy as np

# ---------------- UI ----------------
st.title("AI Manufacturing Defect Generator")

process = st.selectbox(
    "Select Process",
    ["welding", "casting"]
)

defect = st.selectbox(
    "Select Defect",
    ["crack", "porosity"]
)

severity = st.selectbox(
    "Select Severity",
    ["low", "medium", "high"]
)

# ---------------- IMAGE GENERATION ----------------
def generate_image(process, defect, severity):
    try:
        folder = "images"

        # Find matching images
        files = [
            f for f in os.listdir(folder)
            if process in f and defect in f
        ]

        if not files:
            return None, "No matching images found"

        selected_file = random.choice(files)
        image_path = os.path.join(folder, selected_file)
        image = Image.open(image_path)

        return image, selected_file

    except Exception as e:
        return None, str(e)

# ---------------- SSIM FUNCTION ----------------
def calculate_ssim(img1, img2):
    img1 = img1.resize((256, 256)).convert("L")
    img2 = img2.resize((256, 256)).convert("L")

    arr1 = np.array(img1)
    arr2 = np.array(img2)

    score, _ = ssim(arr1, arr2, full=True)
    return score

# ---------------- BUTTON ----------------
if st.button("Generate Image"):

    image, filename = generate_image(process, defect, severity)

    if image:
        st.image(image, caption=f"{process} with {defect} ({severity})")

        # --- REFERENCE IMAGE (IMPORTANT) ---
        ref_path = f"images/{process}_{defect}_1.png"

        if os.path.exists(ref_path):
            ref_img = Image.open(ref_path)

            score = calculate_ssim(image, ref_img)

            st.write(f"### SSIM Score: {score:.3f}")

            if score > 0.8:
                st.success("High similarity (Good quality)")
            elif score > 0.5:
                st.warning("Moderate similarity")
            else:
                st.error("Low similarity")

        else:
            st.warning("Reference image not found for SSIM")

    else:
        st.error(filename)