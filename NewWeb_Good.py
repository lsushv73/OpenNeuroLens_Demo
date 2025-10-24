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
IMG_PATH = BASE_DIR / "static" / "EEGB" / "ONL.png"

# -------------------------------
# Show image
# -------------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if IMG_PATH.exists():
        st.image(str(IMG_PATH), width=250)
    else:
        st.error(f"⚠️ Image not found: {IMG_PATH}")

# -------------------------------
# Directories
# -------------------------------
STATIC_DIR = BASE_DIR / "static"
EEGB_DIR = STATIC_DIR / "EEGB"
DEMO_DIR = STATIC_DIR / "Demo"

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

    # -------------------------------
    # Configuration Settings
    # -------------------------------
    st.markdown("## ⚙️ Configuration Settings")

    # --- 1. File Settings ---
    with st.expander("📁 File Settings", expanded=False):
        file_type = st.selectbox(
            "EEG File Type: Choose the input EEG file format",
            ["BrainVision (.vhdr/.eeg/.vmrk)", "EDF (.edf)", "BDF (.bdf)", "EEGLAB (.set)", "CSV (.csv)"],
            index=0,
        )
        sampling_rate = st.selectbox(
            "Sampling Rate (Hz): Sampling rate determines temporal resolution of EEG data",
            ["256", "512", "1024", "2048"],
            index=1,
        )
        channel_count = st.selectbox(
            "Number of Channels: Specify the total number of EEG electrodes used",
            ["32", "64", "128", "256"],
            index=1,
        )

    # --- 2. Preprocessing Settings ---
    with st.expander("🧩 Preprocessing Settings", expanded=False):
        filter_band = st.selectbox(
            "Filter Band: Frequency range to retain during preprocessing",
            ["0.1–30 Hz", "0.5–40 Hz", "1–50 Hz", "Custom"],
            index=1,
        )
        notch_filter = st.selectbox(
            "Notch Filter: Removes powerline noise (typically 50 or 60 Hz)",
            ["None", "50 Hz", "60 Hz"],
            index=2,
        )
        reref = st.selectbox(
            "Re-reference: Sets the reference channel or average reference method",
            ["Average", "Linked Mastoids", "None"],
            index=0,
        )

    # --- 3. Epoching Settings ---
    with st.expander("🪄 Epoching Settings", expanded=False):
        epoch_window = st.selectbox(
            "Epoch Window: Defines the time interval around each event marker",
            ["-200 to 800 ms", "-100 to 1000 ms", "-500 to 1500 ms"],
            index=0,
        )
        event_channel = st.selectbox(
            "Event Channel: Selects the event channel used to mark stimuli or responses",
            ["Stimulus", "Response", "Custom"],
            index=0,
        )
        baseline_corr = st.selectbox(
            "Baseline Correction: Whether to normalize each epoch to its pre-stimulus baseline",
            ["Yes", "No"],
            index=0,
        )

    # --- 4. Artifact Rejection ---
    with st.expander("🚫 Artifact Rejection", expanded=False):
        artifact_reject = st.selectbox(
            "Artifact Rejection Method: Selects automatic or manual artifact removal",
            ["Automatic", "Manual", "None"],
            index=0,
        )
        threshold_uv = st.selectbox(
            "Amplitude Threshold (µV): Rejects data exceeding this voltage threshold",
            ["75", "100", "125", "150"],
            index=1,
        )
        blink_detection = st.selectbox(
            "Blink Detection: Enable automatic detection of blink artifacts",
            ["Enabled", "Disabled"],
            index=0,
        )

    # --- 5. Channel Settings ---
    with st.expander("📡 Channel Settings", expanded=False):
        montage_type = st.selectbox(
            "Montage Type: Defines electrode positioning system (e.g., 10-20)",
            ["Standard 10-20", "Standard 10-10", "Custom"],
            index=0,
        )
        bad_channel_interp = st.selectbox(
            "Interpolate Bad Channels: Reconstructs noisy channels using neighboring electrodes",
            ["Yes", "No"],
            index=0,
        )
        ref_channel = st.selectbox(
            "Reference Channel: Specifies which electrode serves as reference",
            ["Cz", "Average", "M1-M2"],
            index=1,
        )

    # --- 6. Analysis Settings ---
    with st.expander("🧠 Analysis Settings", expanded=False):
        analysis_type = st.selectbox(
            "Analysis Type: Choose the main analysis type (ERP, PSD, etc.)",
            ["ERP", "PSD", "Time-Frequency", "Connectivity"],
            index=0,
        )
        time_window = st.selectbox(
            "Time Window: Selects the time range for analysis",
            ["0–500 ms", "0–800 ms", "Custom"],
            index=0,
        )
        frequency_range = st.selectbox(
            "Frequency Range: Specify which frequency band to analyze",
            ["Delta (1–4 Hz)", "Theta (4–8 Hz)", "Alpha (8–13 Hz)", "Beta (13–30 Hz)", "Gamma (30–80 Hz)"],
            index=2,
        )

    # --- 7. Output Settings ---
    with st.expander("💾 Output Settings", expanded=False):
        export_format = st.selectbox(
            "Export Format: Choose the format to save processed EEG data",
            ["Excel (.xlsx)", "CSV (.csv)", "JSON (.json)"],
            index=0,
        )
        include_figures = st.selectbox(
            "Include Figures in Output: Include generated figures in the export file",
            ["Yes", "No"],
            index=0,
        )
        auto_download = st.selectbox(
            "Enable Auto-Download: Automatically download results after processing",
            ["Yes", "No"],
            index=1,
        )

    # --- 8. Display Options ---
    with st.expander("🖥️ Display Options", expanded=False):
        theme_mode = st.selectbox(
            "Theme Mode: Switch between light, dark, or system theme",
            ["Light", "Dark", "System Default"],
            index=0,
        )
        show_annotations = st.selectbox(
            "Show Annotations on Plots: Display event or region markers on plots",
            ["Yes", "No"],
            index=0,
        )
        figure_size = st.selectbox(
            "Figure Size: Controls the overall plot size",
            ["Small", "Medium", "Large"],
            index=1,
        )

    # --- 9. Logging & Debug ---
    with st.expander("📋 Logging & Debug", expanded=False):
        log_level = st.selectbox(
            "Log Level: Controls the verbosity of log messages",
            ["INFO", "DEBUG", "WARNING", "ERROR"],
            index=0,
        )
        save_logs = st.selectbox(
            "Save Log File: Option to save processing logs for later review",
            ["Yes", "No"],
            index=1,
        )
        show_console_output = st.selectbox(
            "Show Console Output: Display logs and system messages during processing",
            ["Yes", "No"],
            index=0,
        )

    # --- 10. Advanced Settings ---
    with st.expander("⚙️ Advanced Settings", expanded=False):
        parallel_processing = st.selectbox(
            "Enable Parallel Processing: Use multiple CPU cores for faster computation",
            ["Yes", "No"],
            index=0,
        )
        gpu_acceleration = st.selectbox(
            "Use GPU (if available): Enable GPU acceleration for supported operations",
            ["Yes", "No"],
            index=1,
        )
        cache_results = st.selectbox(
            "Cache Results: Store computed results to speed up future runs",
            ["Yes", "No"],
            index=0,
        )

    st.markdown("---")

    # -------------------------------
    # Process Button
    # -------------------------------
    if st.button("🚀 Process"):
        st.markdown("### EEG Processing Results")

        progress_text = st.empty()
        progress_bar = st.progress(0)
        for percent_complete in range(101):
            time.sleep(0.03)
            progress_bar.progress(percent_complete)
            progress_text.text(f"Processing... {percent_complete}%")
        progress_text.text("✅ Processing complete!")

        # EEG result images
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
    ("", "EEG1", "EEG2"),
    horizontal=True
)

EXAMPLE_DIRS = {
    "EEG1": BASE_DIR / "static" / "Example1",
    "EEG2": BASE_DIR / "static" / "Example2"
}

if eeg_choice:
    st.success(f"{eeg_choice} selected")
    example_path = EXAMPLE_DIRS[eeg_choice]
    st.markdown("### 📈 EEG Figures")

    image_files = sorted(list(example_path.glob("*.png")) + list(example_path.glob("*.jpg")) + list(example_path.glob("*.jpeg")))
    if image_files:
        for img_file in image_files:
            st.image(str(img_file), caption=img_file.name, use_container_width=True)
    else:
        st.warning(f"⚠️ No EEG images found in {example_path}")

    st.markdown("---")
    st.markdown("### 📊 EEG Analysis Results (Excel Preview)")
    excel_files = list(example_path.glob("*.xlsx"))
    if excel_files:
        excel_path = excel_files[0]
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
