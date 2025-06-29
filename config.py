import os
from dotenv import load_dotenv

load_dotenv('../.env')
TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('EXCHANGE_API_KEY')