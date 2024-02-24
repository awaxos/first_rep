# import asyncio
# import logging
# import sys
#
# from datetime import datetime, timedelta, date, time
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message
#
# TOKEN = '6333492425:AAEPhavOYXmAEon43siELnx9iBijHFAjBFs'
# dp = Dispatcher()
#
#
# @dp.message(F.text == '/date')
# async def times(message: Message):
#     result = str(date.today())
#     await message.answer(result)
#
#
# async def main() -> None:
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())

#####################################################################################################################
#2 - task
#####################################################################################################################
# import asyncio
# import logging
# import sys
#
# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# from redis_dict import RedisDict
#
# TOKEN = '6333492425:AAEPhavOYXmAEon43siELnx9iBijHFAjBFs'
# dp = Dispatcher()
# Admin = 5736483354
# info = RedisDict()
#
#
# @dp.message()
# async def informations(message: Message):
#     user = message.from_user
#     info[str(user.id)] = {
#         'first_name': user.first_name,
#         'username': user.username
#     }
#     print(info)
#
#
# async def main() -> None:
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())

#####################################################################################################################
#3 - task
####################################################################################################################

# import asyncio
# import logging
# import sys
#
# from aiogram import Bot, Dispatcher, F
# from aiogram.enums import ParseMode, InputMediaType, ContentType
# from aiogram.filters import CommandStart
# from aiogram.types import Message, KeyboardButton, URLInputFile, InlineKeyboardButton, CallbackQuery, \
#     ReplyKeyboardRemove, InputMediaPhoto, InputFile
# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
# from redis_dict import RedisDict
#
# TOKEN = '6333492425:AAEPhavOYXmAEon43siELnx9iBijHFAjBFs'
# dp = Dispatcher()
# Admin = 5736483354
# info1 = RedisDict()
#
#
# @dp.message(CommandStart())
# async def informations(message: Message):
#     rkm = ReplyKeyboardBuilder()
#     rkm.add(KeyboardButton(text="A`zo bo`lish"))
#     await message.answer("A`zo bo`lish uchun shu tugmachani bosing.", reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.message(F.text == "A`zo bo`lish")
# async def azolar(message: Message):
#     user = message.from_user
#     info1[str(user.id)] = {
#         'first_name': user.first_name,
#         'last_name': user.last_name,
#         'username': user.username
#     }
#     await message.answer("Siz muvaffaqiyat;i azo bo`ldingiz")
#
#
#
# @dp.message(F.text == '/check')
# async def admin(message: Message):
#     a = 0
#     for i in info1:
#         a += 1
#     msg = f'A`zo bo`lganlar soni {a}:\n'
#     await message.answer(msg)
#     print(info1)
#
#
# async def main() -> None:
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())

#####################################################################################################################
# 4 - task
#####################################################################################################################

# import asyncio
# import logging
# import sys
# import time
#
# from datetime import datetime, timedelta, date, time
# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import CommandStart
# from aiogram.types import Message
#
# TOKEN = '6333492425:AAEPhavOYXmAEon43siELnx9iBijHFAjBFs'
# dp = Dispatcher()
#
#
# @dp.message(F.text == '/time')
# async def times(message: Message):
#     result = str(datetime.now())
#     await message.answer(result)


# async def main() -> None:
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())

######################################################################################################################
#1 - task
#######################################################################################################################

