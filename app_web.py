import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

# Apply background
set_bg()

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
st.markdown("#### If you don't have valid EEG files, you may")
st.markdown("## Explore the Following Example EEG Datasets")

eeg_choice = st.radio(
    "Choose EEG data to explore:",
    ("EEG1", "EEG2", "EEG3"),
    horizontal=True
)

if eeg_choice:
    st.success(f"{eeg_choice} selected")

    # Simulated EEG data
    x = np.linspace(0, 1, 500)
    eeg_data = {
        "EEG1": [np.sin(10 * np.pi * x), np.sin(15 * np.pi * x), np.cos(10 * np.pi * x), np.cos(15 * np.pi * x)],
        "EEG2": [np.sin(8 * np.pi * x), np.sin(12 * np.pi * x), np.cos(8 * np.pi * x), np.cos(12 * np.pi * x)],
        "EEG3": [np.sin(6 * np.pi * x), np.sin(9 * np.pi * x), np.cos(6 * np.pi * x), np.cos(9 * np.pi * x)],
    }

    signals = eeg_data[eeg_choice]

    st.markdown("### Show EEG Figures")

    col1, col2 = st.columns(2)
    with col1:
        show_fig1 = st.checkbox("Show Figure 1")
        show_fig2 = st.checkbox("Show Figure 2")
    with col2:
        show_fig3 = st.checkbox("Show Figure 3")
        show_fig4 = st.checkbox("Show Figure 4")

    # Plot figures
    if show_fig1:
        fig1, ax1 = plt.subplots()
        ax1.plot(x, signals[0])
        ax1.set_title(f"{eeg_choice} - Figure 1")
        st.pyplot(fig1)

    if show_fig2:
        fig2, ax2 = plt.subplots()
        ax2.plot(x, signals[1], color='orange')
        ax2.set_title(f"{eeg_choice} - Figure 2")
        st.pyplot(fig2)

    if show_fig3:
        fig3, ax3 = plt.subplots()
        ax3.plot(x, signals[2], color='green')
        ax3.set_title(f"{eeg_choice} - Figure 3")
        st.pyplot(fig3)

    if show_fig4:
        fig4, ax4 = plt.subplots()
        ax4.plot(x, signals[3], color='red')
        ax4.set_title(f"{eeg_choice} - Figure 4")
        st.pyplot(fig4)

    st.markdown("---")

    # -------------------------------
    # Simulated Excel Table
    # -------------------------------
    show_table = st.checkbox("Show analysis results table (xlsx preview)")
    if show_table:
        sheets = {
            "Summary": pd.DataFrame({
                "Metric": ["Theta", "Alpha", "Beta"],
                "Power (µV²)": [12.3, 8.5, 5.7],
                "Change (%)": [5.1, -2.3, 1.8]
            }),
            "ERP Peaks": pd.DataFrame({
                "Component": ["N2", "P3"],
                "Latency (ms)": [240, 380],
                "Amplitude (µV)": [-4.2, 6.8]
            }),
            "Metadata": pd.DataFrame({
                "Subject": ["S01", "S02", "S03"],
                "Session": ["Pre", "Post", "Post"],
                "Condition": ["Go", "NoGo", "Go"]
            })
        }

        st.write("### 📊 Multi-Tab Table Preview")
        tabs = st.tabs(list(sheets.keys()))

        for i, tab in enumerate(tabs):
            with tab:
                st.dataframe(sheets[list(sheets.keys())[i]])
else:
    st.info("Select an EEG dataset to begin.")
