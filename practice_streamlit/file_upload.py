import streamlit as st
import pandas as pd

file = st.file_uploader("Upload your File ")

if file:
    df = pd.read_csv(file)
    st.dataframe(df.head( ))