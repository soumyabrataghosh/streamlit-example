from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Lustro22 Servey!

### Enter your token
"""

token_url_df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjT51_uvt-sBRfDBdrWJCiCTspKxEtZTihm3RPb1YqtErzjSHbd1Sz0UZChsefSW1lD-z4Q66M4275/pub?output=csv')

token = st.text_input('TOKEN', '')
st.button('Submit')
if token == '':
    pass
elif token_url_df['Token'].isin([token]).any().any():
    st.write('Go to your servey:')
    st.write(list(token_url_df.loc[token_url_df['Token']==token]['Invite Link'])[0])
else:
    st.write('Not a valid token')




            
