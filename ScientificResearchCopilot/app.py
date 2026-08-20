import streamlit as st
import numpy as np
import pandas as pd

from analysis.transport import classify_transport


st.title("🔬 Scientific Research Copilot")

st.write("Experimental Condensed Matter Physics")

st.header("Transport Analysis")

# Upload experimental data
uploaded_file = st.file_uploader(
    "Upload R(T) data",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    st.subheader("Uploaded Data")

    st.dataframe(data)

    st.write("Columns detected:", list(data.columns))

    temperature_column = None
    resistance_column = None

    for column in data.columns:
        name = str(column).lower()

        if "temp" in name or name in ["t", "temperature (k)", "t (k)"]:
            temperature_column = column

        if "res" in name or "resistance" in name or name in ["r", "r (ohm)", "r (ω)"]:
            resistance_column = column

    if temperature_column is not None:
        st.success(f"Temperature column detected: {temperature_column}")
    else:
        st.warning("Temperature column could not be identified.")

    if resistance_column is not None:
        st.success(f"Resistance column detected: {resistance_column}")
    else:
        st.warning("Resistance column could not be identified.")

else:
    st.info("Upload a CSV or Excel file containing Temperature and Resistance data.")