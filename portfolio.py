import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.title("Similars annotations")

catalog = ["A cat", "A dog", "A pidgeon"]


titles = st.multiselect("Chosen similar titles", options=catalog)

if st.button("Choose"):
    st.write(titles)


col1, col2 = st.columns(2)

with col1:
    st.header("A cat")


with col2:
    st.header("A dog")
