!pip install bokeh
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

if st.button('SUBMIT'):
    if token_url_df['Token'].isin([token]).any().any():
        url = list(token_url_df.loc[token_url_df['Token']==token]['Invite Link'])[0]
        #js = "window.open('https://www.streamlit.io/')"  # New tab or window
        js = "window.location.href = '"+str(url)+"'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)


if token == '':
    pass
elif token_url_df['Token'].isin([token]).any().any():
    st.write('Go to your servey:')
    st.write(list(token_url_df.loc[token_url_df['Token']==token]['Invite Link'])[0])
else:
    st.write('Not a valid token')

    
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


            
