import http
from imaplib import _Authenticator
from xml import dom
import dotenv
from pathlib import Path
import streamlit_authenticator as stauth
from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
import numpy as np
import pandas as pd
import random


#------PAGE--------

st.set_page_config(
    page_title="Chatbot",
    page_icon="👋",
)

logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Infosys_logo.svg/2560px-Infosys_logo.svg.png"
st.sidebar.image(logo_url, use_column_width=True)

#--------SECRETS--------------

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os
with st.sidebar: 
# Define your config here
    config = {
        'credentials': {
            'usernames': {
                'jsmith': {
                    'email': 'jsmith@example.com',
                    'name': 'John Smith',
                    'password': 'hashed_password_here'  # This should be hashed in a real application
                },
                'rbriggs': {
                    'email': 'rbriggs@example.com',
                    'name': 'Rebecca Briggs',
                    'password': 'hashed_password_here'  # This should be hashed in a real application
                }
            }
        },
        'cookie': {
            'expiry_days': 30,
            'key': 'some_signature_key',
            'name': 'some_cookie_name'
        }
    }

    # Create an authentication object
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'], 
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        
    )

    # Render the login widget
    name, authentication_status, username = authenticator.login()

    # Handle authentication status
    if authentication_status:
        st.write(f'Welcome *{name}*')
        st.title('Some content')
        authenticator.logout('Logout', 'main')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')
    




#----------------CHATBOT----------------
def ChatUI():
    env_path = r"/Users/ed_chat_bot/chatbot_project/.env"

    load_dotenv(env_path)
    API_KEY = os.getenv('API_KEY')
    print (API_KEY)

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    def generate_content(prompt):
            response = model.generate_content(prompt)
            return response.text

    prompt = st.text_input('Enter a prompt:')
    if st.button('Generate'):
            response = generate_content(prompt)
            st.write (response)

#-----DEFINING TABS-----ƒf
    
tab1, tab2,tab3,tab4,tab5, = st.tabs(["ChatUI","Math", "English"," History","Science,"])
tab1.title("ChatUI")
tab2.title("Math")
tab3.title("English")
tab4.title("History")
tab5.title("Science")
#-------SPREADSHEET---------

from streamlit_gsheets import GSheetsConnection
from pandas import DataFrame
conn = st.connection("gsheets", type=GSheetsConnection)

def database():
    st.title = "Database"
    url = "https://docs.google.com/spreadsheets/d/1b4AOJhDZbOa_NnlQWkwdbc2MqqyDZlOss5d1UhsRZzU/edit?usp=sharing"
   
    with tab1:
        st.header("New Assignments")
        st.write("Math: Pop quiz")
        st.write("English: Read & Write")
        st.write("History: Tea Tax")

        st.header("Recently Graded Assignmenst")
        st.write("Math: Basic trig formulas")
        st.write("English: Indapendent Reading")
        st.write("History: Bostan Tea party")
        st.write("Science: Periodic Table")

   
    with tab2:
        st.header("C-")
       
        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="764048703",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="0",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)
        st.line_chart(data1)



     
       
       
    
    with tab3:
        st.header("B-")
        
        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1776590617",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="525292218",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)
        st.line_chart(data1)
       
       
    
    with tab4:
        st.header("B+")

        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1251738910",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="1395020218",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)
        st.line_chart(data1)
    
    
    with tab5:
        st.header("F")

        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1251738910",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="1395020218",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)
        st.line_chart(data1)

    


#--------Markdown--------
page_names_to_funcs = {
    ("ChatUI"): ChatUI,
     ("Database"): database,
    
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()




