import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/Myphoto.jpeg")

with col2:
    st.title("Charanjeet Singh")
    content = """Hi, I am Charanjeet! I am a Python Programmer, Data Analyst, Traveller.
    I have worked in different spaces like Data analysis, Market Research, Recruitment, BI developer
    and now Python Programmer."""
    st.info(content)


content2 = "Below you can find some of the apps I have built in Pytho. Feel free to contact me!"
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://www.google.com))")