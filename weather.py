import os
import datetime
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor 

bot = Bot(token='1')
dp= Dispatcher(bot)

@dp
print("Сегодня матчей нет.") 

