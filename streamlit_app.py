import pandas as pd
import streamlit as st
"""
# Welcome to Lustro22 Servey!

### Enter your token
"""
def print_hi():
    st.error('Hello')

token_url_df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjT51_uvt-sBRfDBdrWJCiCTspKxEtZTihm3RPb1YqtErzjSHbd1Sz0UZChsefSW1lD-z4Q66M4275/pub?output=csv')

token = st.text_input('TOKEN', '',max_chars=8)
if st.button('Submit'):
    print_hi()

if token == '':
    pass
elif token_url_df['Token'].isin([token]).any().any():
    url = list(token_url_df.loc[token_url_df['Token']==token]['Invite Link'])[0]
    st.markdown("<a href='"+str(url)+"'> Go to your survey </a>",unsafe_allow_html=True)
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


            
