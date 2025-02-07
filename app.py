import streamlit as st
import pandas as pd

st.title("📊 Excel File Viewer")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("### Preview of Uploaded File:")
    st.dataframe(df)
else:
    st.info("Please upload an Excel file to display its contents.")
