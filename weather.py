import os
import datetime
import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart 

bot = Bot(token='8712024753:AAFLeLHhv_sfVV8qfb123nc_PLFZfcesWHE')
dp= Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.reply("Chouse your city")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())


