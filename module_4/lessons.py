# import requests
# url = 'https://jsonplaceholder.typicode.com/users'
# data = requests.get(url).json()
# headers = data[0].keys()
# d = []
#
# for i in data:
#     d.append(i['id'])
# print(headers)

# s = input()
# a = ''
#
# for i in range(len(s)):
#     if s[-1] == s[i] and s[-2] == s[i] and s[i] == s[-3]:
#         continue
#     elif s[i] == s[i + 1] and s[i] == s[i + 2]:
#         print(s[i])

# s = input().split()
# a = ''
# s = set(s)
#
# print(s)

import asyncio
import logging
import smtplib
import ssl
import sys
from random import randint
import requests
import json

from aiogram import Bot, Dispatcher, F
from aiogram.enums import content_type
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

TOKEN = '6493144199:AAFkXLBiekNJLH8eJwGre8YbzVjGe6N5eds'  # https://t.me/p19_proverka_bot
dp = Dispatcher()


@dp.message(CommandStart())
async def informations(message: Message):




async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())