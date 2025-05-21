import os

from dotenv import load_dotenv

load_dotenv()

# Database settings
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Redis settings
REDIS_URL=os.getenv("REDIS_URL")

# Bot settings
BOT_TOKEN = os.getenv("BOT_TOKEN")

# OpenAI settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# All links that are used in the project.
URLS = {
    'KC_BASE': 'https://xn--80adxqo3a.xn--p1ai/state/G_%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B/E_%D0%9D%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE-%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%B1%D0%B0%D0%B7%D0%B0',
    'CONSULTING_APPOINTMENT': 'https://xn--80adxqo3a.xn--p1ai/#segment_30',
    'PORTAL': 'https://xn--80aidamjr3akke.xn--p1ai/',
    'YANDEX_FORM': 'https://forms.yandex.ru/u/672e5bb584227c79f8f9cc95/',
    'FEEDBACK_TO_EXPERT': 'https://xn--80adxqo3a.xn--p1ai/review',

    'VK_GROUP': 'https://vk.com/roditelgostinaya'
}
