import streamlit as st

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

st.write("Below you can find some of the apps I have built in Pytho. Feel free to contact me!")