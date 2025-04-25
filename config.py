import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import aiomysql
from aiogram import Bot, Dispatcher, Router

load_dotenv()
TOKEN = os.getenv("TOKEN")
API_KEY = os.getenv("API_KEY")
DBPASSWORD = os.getenv("DBPASSWORD")
HOST=os.getenv("HOST")
USER=os.getenv("USER")
DATABASE=os.getenv("DATABASE")
TEMPERATURE = 1.5

START_MESSAGE = "Привет! Я дедушка Дрёма — самый интересный рассказчик на свете! ✨ \n\nЯ могу сочинять сказки про твоих любимых героев. А ты сможешь подсказывать, какие приключения их будут ждать дальше! \n\nСкажи, как тебя зовут и что ты любишь, и я приготовлю сказку специально для тебя. Для этого заполни свой профиль. ✏️\n\nНу что, начнём? 💫\n"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

client = AsyncOpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

async def get_async_connection():
    try:
        conn = await aiomysql.connect(
            host=HOST,
            user=USER,
            password=DBPASSWORD,
            db=DATABASE,
            charset='utf8mb4',
            autocommit=True
        )
        return conn
    except Exception as e:
        print(f"Ошибка подключения к MySQL: {e}")
        return None