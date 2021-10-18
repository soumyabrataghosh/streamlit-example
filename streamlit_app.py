import pandas as pd
import streamlit as st
"""
# Welcome to Lustro22 Servey!

### Enter your token
"""
def check_token(token_url_df_in,token_in):
    if token_in == '':
        st.error('Enter a token')
    elif token_url_df_in['Token'].isin([token_in]).any().any():
        url = list(token_url_df_in.loc[token_url_df['Token']==token_in]['Invite Link'])[0]
        st.markdown("<div role='alert' data-baseweb='notification' class='st-ae st-af st-ag st-ah st-ai st-aj st-ak st-cm st-am st-b8 st-ao st-ap st-aq st-ar st-as st-at st-cn st-av st-aw st-ax st-ay st-az st-b9 st-b1 st-b2 st-b3 st-b4 st-b5 st-co'> <a href='"+str(url)+"'> Go to your survey </a> </div>", unsafe_allow_html=True)
    else:
        st.success('Not a valid token')


token_url_df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjT51_uvt-sBRfDBdrWJCiCTspKxEtZTihm3RPb1YqtErzjSHbd1Sz0UZChsefSW1lD-z4Q66M4275/pub?output=csv')

token = st.text_input('TOKEN', '',max_chars=8)
if st.button('Submit'):
    check_token(token_url_df,token)


    
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


            
