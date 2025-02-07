import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
import os

st.title("📊 Large Excel File Viewer (Optimized)")

# Increase file size limit (optional)
st.set_option('server.maxUploadSize', 500)  # 500MB limit

# Upload Excel File
uploaded_file = st.file_uploader("Upload a large Excel file", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Read only first few rows for preview
        df = pd.read_excel(uploaded_file, nrows=1000)
        
        # Save as Parquet (compressed & faster)
        file_path = "large_file.parquet"
        df.to_parquet(file_path, compression='snappy')

        st.success("File uploaded successfully!")
        
        # Display preview
        st.write("### Preview (First 1000 rows):")
        st.dataframe(df)

    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Upload a large Excel file to view its contents.")
