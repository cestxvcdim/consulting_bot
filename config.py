"""This file collects variables from the .env file."""

from os import getenv
from dotenv import load_dotenv

load_dotenv()

db_user = getenv('DB_USER')
password = getenv('PASSWORD')
host = getenv('HOST')
port = getenv('PORT')
db_name = getenv('DB_NAME')

class Config:
    """Code space for variables from .env file"""
    db_path = f"postgresql://{db_user}:{password}@{host}:{port}/{db_name}"
    bot_token = getenv('BOT_TOKEN')
    api_key = getenv('API_KEY')
