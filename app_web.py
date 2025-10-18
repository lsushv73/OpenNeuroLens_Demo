import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("OpenNeuroLens (Demo)")
st.subheader("Low-cost, high-quality EEG analysis platform")

st.markdown("### Upload EEG Data (Demo Mode)")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    st.write("### Simulated Analysis")
    with st.spinner("Running signal analysis..."):
        time.sleep(2)
        st.success("Demo complete!")

        st.line_chart(df.iloc[:, 1:3])  # example plot
else:
    st.info("Please upload a CSV file to begin.")
