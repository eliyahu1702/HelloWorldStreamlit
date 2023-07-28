import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

dict = {"a": "alpha", "o": "omega", "g": "gamma"}

st.header("St Button Time")
button = st.button(label="hello button")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))
st.write(dict)
st.write('Hello, *World!* :sunglasses:')
df = pd.DataFrame(
    np.random.randn(200, 4),
    columns=['a', 'b', 'c','d'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='d', tooltip=['a', 'b', 'c'])
st.write(c)

