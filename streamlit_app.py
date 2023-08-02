import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
errormessage = "Username or Password **INVALID**"
# url = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=3DpS4ivuJ1bempfR2_KN8lcboNLDUZMQ"
# response = requests.get(url)
# j = json.loads(response.text)
# df = pd.DataFrame(j) 
# pd.json_normalize(df["results"])  
# st.write(df)
with st.sidebar:
    username = st.text_input("username")
    password = st.text_input("password",type="password")
    col1, col2 = st.columns(2)
    with col1:
        login_button = st.button("log in")
    with col2:
        sign_up_button = st.button("sign up")
    if login_button and (username == '' or password ==''):
           st.write(f':red[{errormessage}]')
    coffee_theme = st.checkbox("coffee theme :coffee:")
    if coffee_theme:
        st.code(
            """
            [theme]
            primaryColor="#d2c1b0"
            backgroundColor="#80411e"
            secondaryBackgroundColor="#37251b"
            textColor="#e4bc84"
            """
        )
if username != '' and password!='' and login_button:
   st.header("Welcome "+ username)
st.subheader('Input CSV Or excel file ')
uploaded_file = st.file_uploader("Choose a file")


if uploaded_file is not None:
  try:
    df = pd.read_csv(uploaded_file)
  except:
    df = pd.read_excel(uploaded_file)  
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  pr = df.profile_report()
  st_profile_report(pr)
else:
  st.info('☝️ Upload a CSV file')


# temperature = "-10"

# st.write(f"temprature: :blue[{temperature}]")
# answer =  st.slider("what's 9 + 10? ",min_value=0, max_value=100)
# chart_data = pd.read_csv("Book.csv",index_col="Time")
# new_chart = chart_data.head(answer)
# st.line_chart(new_chart)
# if answer == 21:
#     st.header("You Stupid")

