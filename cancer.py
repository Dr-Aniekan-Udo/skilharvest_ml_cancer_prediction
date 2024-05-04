import streamlit as st
from PIL import Image
import machine
from machine import selected
import pandas as pd
import numpy as np
import sklearn
import warnings
warnings.filterwarnings("ignore")


#set up the page appearnace for streamlit
st.set_page_config(layout = "wide")
#let's write the markdown setup
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html= True)
#let's import our image \
image = Image.open(r'C:\Users\anibr\Desktop\skillharvest\final\cancer.jpg')

#let's create columns  where our charts will be displayed
col1, col2 = st.columns([0.1,0.9])

#edit each columnsto appropriate appearance
with col1:
    st.image(image,width = 100)
#let's write an html title
html_title = """
    <style>
    .title-test{
    font-weight:bold;
    padding:5px;
    border-radius:6px}
    </style>
    <center><h1 class = "title-test">AI-powered Cancer Prediction Software</h1></center>"""
with col2:
    st.markdown(html_title, unsafe_allow_html = True)

st.subheader('Required parameters form')
input={}
for i in machine.selected:
    input[i]=[0]
expander = st.expander('fill the form')
with expander.form("Enter the histology details"):
    for i in input:
        input[i]=[st.number_input(i)]
    button = st.form_submit_button('submit')
if button:
    test = pd.DataFrame(input)
    st.dataframe(test)
    result=machine.execute(test)
    st.write("Result:",result)
        
