import os
from dotenv import load_dotenv

# command to call your gemeni API key using dotenv. Make sure you add your API key to the .env file
gemini_pro_api_key = os.getenv('GEMINI_PRO_API_KEY')
