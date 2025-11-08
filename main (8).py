import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

# Замените на ваш токен от @BotFather
BOT_TOKEN = '8251195826:AAFYE8kzLiOeaX3QqgYrfsrTEwd-GIa-NDQ'
# Замените на URL вашего Vercel-приложения (например, https://mono-telegram.vercel.app)
WEB_APP_URL = "https://mono-telegram.vercel.app"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

@router.message()
async def send_welcome(message: Message):
    button = InlineKeyboardButton(
        text="📚 Начать учить слова",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer("Привет! Давай изучать английский с Mono 🧠", reply_markup=keyboard)

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())