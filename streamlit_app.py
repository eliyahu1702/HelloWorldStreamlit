import streamlit as st
import openpyxl
import pandas as pd
import numpy as np
import altair as alt


dict = {"a": "alpha", "o": "omega", "g": "gamma"}
st.header("slider time")
answer =  st.slider("what's 9 + 10?",min_value=0, max_value=100)
chart_data = pd.read_csv("Book.csv",index_col="Time")
new_chart = chart_data.head(answer)
st.line_chart(new_chart)
if answer == 21:
    st.header("You Stupid")

