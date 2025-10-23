import streamlit as st
from pathlib import Path
import pandas as pd
import time

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
STATIC_DIR = BASE_DIR / "static"
EEGB_DIR = STATIC_DIR / "EEGB"
DEMO_DIR = STATIC_DIR / "Demo"

# -------------------------------
# Background Image
# -------------------------------
def set_bg():
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

set_bg()

# -------------------------------
# Session state for login
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------------
# Main App Function
# -------------------------------
def main_app():
    st.title("Welcome to OpenNeuroLens (Demo)")
    st.subheader("Low-cost, high-quality EEG analysis platform")
    st.markdown("---")

    # Upload EEG section
    st.markdown("## 🧠 Upload Your EEG File")
    uploaded_file = st.file_uploader(
        "Choose an EEG file",
        type=["eeg", "edf", "bdf", "set", "vhdr", "cnt", "csv"]
    )

    if uploaded_file is not None:
        st.success(f"✅ Uploaded file: {uploaded_file.name}")
        if st.button("🚀 Process"):
            st.markdown("### EEG Processing Results")
            progress_text = st.empty()
            progress_bar = st.progress(0)
            for percent_complete in range(101):
                time.sleep(0.03)
                progress_bar.progress(percent_complete)
                progress_text.text(f"Processing... {percent_complete}%")
            progress_text.text("✅ Processing complete!")

    st.markdown("---")

    # Example EEG datasets
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
        image_files = sorted(list(example_path.glob("*.png")) +
                             list(example_path.glob("*.jpg")) +
                             list(example_path.glob("*.jpeg")))
        if image_files:
            for img_file in image_files:
                st.image(str(img_file), caption=img_file.name, use_container_width=True)
        else:
            st.warning(f"⚠️ No EEG images found in {example_path}")

        st.markdown("### 📊 EEG Excel Results (Excel Preview)")
        excel_files = list(example_path.glob("*.xlsx"))
        if excel_files:
            excel_path = excel_files[0]
            try:
                excel_data = pd.read_excel(excel_path, sheet_name=None)
                tabs = st.tabs(list(excel_data.keys()))
                for i, tab_name in enumerate(excel_data.keys()):
                    with tabs[i]:
                        st.dataframe(excel_data[tab_name])
            except Exception as e:
                st.error(f"Error reading Excel file: {e}")
        else:
            st.warning(f"⚠️ No Excel (.xlsx) file found in {example_path}")
    else:
        st.info("Select an EEG dataset to begin.")

# -------------------------------
# Login Section
# -------------------------------
if not st.session_state.logged_in:
    st.title("EEG Data Explorer Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "test1" and password == "password1":
            st.session_state.logged_in = True
            st.success("Login successful! ✅")
        else:
            st.error("❌ Invalid username or password.")
else:
    main_app()  # Show main app only if logged in
