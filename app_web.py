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
# Paths
# -------------------------------
BASE_DIR = Path(__file__).parent
IMG_PATH = BASE_DIR / "static" / "EEGB" / "ONL.png"  # adjust path if needed

# -------------------------------
# Show image
# -------------------------------
if IMG_PATH.exists():
    #st.image(str(IMG_PATH), use_column_width=True)
    st.image(str(IMG_PATH), use_container_width=True)
else:
    st.error(f"⚠️ Image not found: {IMG_PATH}")

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

        for percent_complete in range(101):
            time.sleep(0.03)  # 100 * 0.03s = 3s total
            progress_bar.progress(percent_complete)
            progress_text.text(f"Processing... {percent_complete}%")

        progress_text.text("✅ Processing complete!")

        

        # EEG result image paths
        result_images = [
            ("ERP_Frontal_GoNoGo.png", "ERP - Frontal Go/NoGo"),
            ("ERP_Posterior_GoNoGo.png", "ERP - Posterior Go/NoGo"),
            ("PSD_Frontal_GoNoGo.png", "Power Spectrum - Frontal Go/NoGo"),
            ("PSD_Posterior_GoNoGo.png", "Power Spectrum - Posterior Go/NoGo"),
        ]

        for img_file, caption in result_images:
            img_path = DEMO_DIR / img_file
            if img_path.exists():
                st.image(str(img_path), caption=caption, use_container_width=True)
            else:
                st.warning(f"⚠️ Missing image: {img_file}")

        # EEG summary Excel file
        xlsx_path = DEMO_DIR / "GoNoGo_summary.xlsx"
        if xlsx_path.exists():
            st.markdown("### 📊 EEG Summary Results (Go/NoGo)")

            try:
                # Load Excel file with multiple sheets
                xls = pd.ExcelFile(xlsx_path)
                sheet_names = xls.sheet_names
                tabs = st.tabs(sheet_names)

                for i, sheet_name in enumerate(sheet_names):
                    with tabs[i]:
                        df = pd.read_excel(xls, sheet_name=sheet_name)
                        st.dataframe(df, use_container_width=True)

            except Exception as e:
                st.error(f"Error reading Excel file: {e}")

        else:
            st.warning("⚠️ EEG summary file 'GoNoGo_summary.xlsx' not found.")


else:
    st.info("👆 Upload an EEG file to begin processing.")

st.markdown("---")

# -------------------------------
# Explore Example EEG Datasets
# -------------------------------
# -------------------------------
# Explore Example EEG Datasets
# -------------------------------
st.markdown("#### If you don't have valid EEG files, you may")
st.markdown("## Explore the Following Example EEG Datasets")

eeg_choice = st.radio(
    "Choose EEG data to explore:",
    ("", "EEG1", "EEG2"),
    horizontal=True
)

# Base path for examples
BASE_DIR = Path(__file__).parent
EXAMPLE_DIRS = {
    "EEG1": BASE_DIR / "static" / "Example1",
    "EEG2": BASE_DIR / "static" / "Example2"
}

if eeg_choice:
    st.success(f"{eeg_choice} selected")

    example_path = EXAMPLE_DIRS[eeg_choice]
    # st.markdown(f"### Showing data from `{example_path}`")

    # -------------------------------
    # Show EEG Figures
    # -------------------------------
    st.markdown("### 📈 EEG Figures")

    # Get all image files (png, jpg, jpeg)
    image_files = sorted(list(example_path.glob("*.png")) + list(example_path.glob("*.jpg")) + list(example_path.glob("*.jpeg")))

    if image_files:
        for img_file in image_files:
            st.image(str(img_file), caption=img_file.name, use_container_width=True)
    else:
        st.warning(f"⚠️ No EEG images found in {example_path}")

    st.markdown("---")

    # -------------------------------
    # Show EEG Excel Results
    # -------------------------------
    st.markdown("### 📊 EEG Analysis Results (Excel Preview)")

    excel_files = list(example_path.glob("*.xlsx"))

    if excel_files:
        excel_path = excel_files[0]  # take first .xlsx file found
        try:
            excel_data = pd.read_excel(excel_path, sheet_name=None)
            tab_names = list(excel_data.keys())
            tabs = st.tabs(tab_names)

            for i, tab in enumerate(tabs):
                with tab:
                    st.dataframe(excel_data[tab_names[i]])
        except Exception as e:
            st.error(f"Error reading Excel file: {e}")
    else:
        st.warning(f"⚠️ No Excel (.xlsx) file found in {example_path}")
else:
    st.info("Select an EEG dataset to begin.")

