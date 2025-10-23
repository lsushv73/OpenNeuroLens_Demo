import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from pathlib import Path

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Welcome to OpenNeuroLens (Demo)",
    layout="centered",
)

# -------------------------------
# Paths (auto-detect project base)
# -------------------------------
BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"
EEGB_DIR = STATIC_DIR / "EEGB"
DEMO_DIR = STATIC_DIR / "Demo"

# -------------------------------
# Background Image
# -------------------------------
def set_bg():
    """Set custom background image from local path."""
    image_path = EEGB_DIR / "EEGB1.jpg"
    if image_path.exists():
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("file://{image_path.resolve()}");
                background-size: cover;
                background-attachment: fixed;
                background-position: center;
                background-repeat: no-repeat;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(f"⚠️ Background image not found at: {image_path}")

set_bg()

# -------------------------------
# Initialize session state
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "login_failed" not in st.session_state:
    st.session_state.login_failed = False

# -------------------------------
# Main App Function
# -------------------------------
def main_app():
    # -------------------------------
    # Welcome Section
    # -------------------------------
    st.title("Welcome to OpenNeuroLens (Demo)")
    st.subheader("Low-cost, high-quality EEG analysis platform")
    st.markdown("---")

    # -------------------------------
    # Upload EEG File Section
    # -------------------------------
    st.markdown("## 🧠 Upload Your EEG File")
    uploaded_file = st.file_uploader(
        "Choose an EEG file",
        type=["eeg", "edf", "bdf", "set", "vhdr", "cnt", "csv"]
    )

    if uploaded_file is not None:
        st.success(f"✅ Uploaded file: {uploaded_file.name}")

        if st.button("🚀 Process"):
            st.markdown("### EEG Processing Results")

            # Progress bar (simulate 3-second processing)
            progress_text = st.empty()
            progress_bar = st.progress(0)
