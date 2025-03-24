import streamlit as st
import pandas as pd
import requests
import os


def upload_and_classify(file):
    # Adjust if your FastAPI server runs on a different host
    url = "http://127.0.0.1:8000/classify/"
    files = {"file": (uploaded_file.name,
                      uploaded_file.getvalue(), "text/csv")}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        with open("output.csv", "wb") as f:
            f.write(response.content)
        return "output.csv"
    else:
        st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        return None


st.title("Log Classification System")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    if st.button("Classify Logs"):
        output_file = upload_and_classify(uploaded_file)
        if output_file:
            st.success("Classification completed. Download the results below.")
            st.download_button(label="Download Output CSV", data=open(
                output_file, "rb"), file_name="output.csv", mime="text/csv")
