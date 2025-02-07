import streamlit as st
import pandas as pd

st.title("📊 Complete Excel File Viewer")

# Path to your existing Excel file
file_path = "extracted_fields.xlsx"

try:
    # Read the entire Excel file
    df = pd.read_excel(file_path)

    # Display table
    st.write("### Full Data Preview:")
    st.dataframe(df)

    # Show basic info
    st.write("### Data Overview:")
    st.write(f"**Rows:** {df.shape[0]}, **Columns:** {df.shape[1]}")

except Exception as e:
    st.error(f"Error loading file: {e}")
