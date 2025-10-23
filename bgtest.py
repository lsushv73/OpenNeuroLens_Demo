# test_image.py
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Image Test", layout="centered")

# -------------------------------
# Path to image
# -------------------------------
BASE_DIR = Path(__file__).parent
IMG_PATH = BASE_DIR / "static" / "EEGB" / "EEGB2.png"  # adjust path if needed

# -------------------------------
# Show image
# -------------------------------
if IMG_PATH.exists():
    st.image(str(IMG_PATH), use_column_width=True)
    st.success("✅ Image loaded successfully!")
else:
    st.error(f"⚠️ Image not found: {IMG_PATH}")

# -------------------------------
# Add some text
# -------------------------------
st.title("Test Page")
st.write("This page shows the EEG1 image using st.image().")
