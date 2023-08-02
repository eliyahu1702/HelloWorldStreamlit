import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

# url = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=3DpS4ivuJ1bempfR2_KN8lcboNLDUZMQ"
# response = requests.get(url)
# j = json.loads(response.text)
# df = pd.DataFrame(j) 
# pd.json_normalize(df["results"])  
# st.write(df)
with st.sidebar:
    coffee_theme = st.checkbox("coffee theme :coffee:")


df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)

answer =  st.slider("what's 9 + 10?",min_value=0, max_value=100)
chart_data = pd.read_csv("Book.csv",index_col="Time")
new_chart = chart_data.head(answer)
st.line_chart(new_chart)
if answer == 21:
    st.header("You Stupid")

