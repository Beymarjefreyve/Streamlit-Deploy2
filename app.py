import streamlit as st
import pandas as pd

st.title("Widgets")

name = st.text_input("Your name")
age = st.slider("Your age", 0, 100, 20)
language = st.selectbox("Favourite language", ["Python", "Java", "C++"])


if st.button("Say hello"):
    st.success(f"Hello {name}! You are {age} and you like {language}.")

st.divider()
file = st.file_uploader("Upload a CSV file", type="csv")
if file is not None:
    df = pd.read_csv(file)
    st.write("Rows:", df.shape[0], "| Columns:", df.shape[1])
    st.dataframe(df.head())
