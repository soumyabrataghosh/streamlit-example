from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from bokeh.models.widgets import Div

"""
# Welcome to Lustro22 Servey!

### Enter your token
"""

token_url_df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjT51_uvt-sBRfDBdrWJCiCTspKxEtZTihm3RPb1YqtErzjSHbd1Sz0UZChsefSW1lD-z4Q66M4275/pub?output=csv')

token = st.text_input('TOKEN', '',max_chars=8)

if token_url_df['Token'].isin([token]).any().any():
    st.button('SUBMIT', on_click="https://google.com")
else:
    st.button('SUBMIT')

if token == '':
    pass
elif token_url_df['Token'].isin([token]).any().any():
    pass
else:
    st.error('Not a valid token')

    
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>app by: \soumya/</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


            
