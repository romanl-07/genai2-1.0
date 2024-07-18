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



#--------SECRETS--------------

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os

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

env_path = r"/Users/ed_chat_bot/chatbot_project/.env"

load_dotenv(env_path)
API_KEY = os.getenv('API_KEY')
print (API_KEY)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
def generate_content(prompt):
        response = model.generate_content(prompt)
        return response.text

st.title('Gemini AI Text Generator')
prompt = st.text_input('Enter a prompt:')
if st.button('Generate'):
        response = generate_content(prompt)
        st.write (response)
        









