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
token_url_df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjT51_uvt-sBRfDBdrWJCiCTspKxEtZTihm3RPb1YqtErzjSHbd1Sz0UZChsefSW1lD-z4Q66M4275/pub?output=csv')
st.dataframe(token_url_df)

token = st.text_input('TOKEN', '')
if token_url_df['Token'].isin([token]).any().any():
    st.write('TOKEN:', token_url_df.loc[token_url_df['Token']==token]['Invite Link'])
else:
    st.write('Not a valid token')




            
