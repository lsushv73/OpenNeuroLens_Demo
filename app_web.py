import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



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
