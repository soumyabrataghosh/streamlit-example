from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

url_dict = {
    'token1':'https://google.com',
    'token2':'https://yahoo.com'
}
token_url_df = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjT51_uvt-sBRfDBdrWJCiCTspKxEtZTihm3RPb1YqtErzjSHbd1Sz0UZChsefSW1lD-z4Q66M4275/pub?output=xlsx')
st.dataframe(token_url_df)

token = st.text_input('TOKEN', '')
if token in url_dict:
    st.write('TOKEN:', url_dict[token])
else:
    st.write('Not a valid token')




            
