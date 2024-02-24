# import asyncio
# import logging
# import smtplib
# import ssl
# import sys
# from random import randint
# import requests
# import json
#
# from aiogram import Bot, Dispatcher, F
# from aiogram.enums import content_type
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, \
#     ReplyKeyboardMarkup, CallbackQuery, URLInputFile
# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
#
# TOKEN = '6333492425:AAEPhavOYXmAEon43siELnx9iBijHFAjBFs'
# dp = Dispatcher()
# products = json.load(open('products.json'))
#
#
# @dp.message(CommandStart())
# async def echo_handler(message: Message):
#     ikm = InlineKeyboardBuilder()
#     ikm.add(InlineKeyboardButton(text="🔙", callback_data="back"))
#     ikm.add(InlineKeyboardButton(text="➕", callback_data="qoshish"))
#     ikm.add(InlineKeyboardButton(text="🔜", callback_data="keyingi"))
#     await message.answer_photo(URLInputFile(products[0]["photo"]), caption=products[0]["caption"], reply_markup=ikm.as_markup())
#
#
# @dp.callback_query(F.data == "keyingi")
# async def keyingisi(call: CallbackQuery):
#     pass
#
# async def main() -> None:
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())


#######################################################################################################################
# bot
#######################################################################################################################

# import asyncio
# import json
# import logging
# import smtplib
# import ssl
# import sys
#
# from aiogram import Bot, Dispatcher, F
# from aiogram.enums import ParseMode, InputMediaType
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.methods import edit_message_reply_markup
# from aiogram.types import Message, KeyboardButton, URLInputFile, InlineKeyboardButton, CallbackQuery, \
#     ReplyKeyboardRemove, InputMediaPhoto, InputFile
# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
#
# TOKEN = '6333492425:AAEPhavOYXmAEon43siELnx9iBijHFAjBFs'
# dp = Dispatcher()
#
# products: list = json.load(open('products.json'))
#
#
# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     _product = products[0]
#     ikm = InlineKeyboardBuilder()
#     ikm.row(*[
#         InlineKeyboardButton(text='⬅️', callback_data=f'{_product["id"] - 1}'),
#         InlineKeyboardButton(text='➕', callback_data=f'plus_{_product["id"]}'),
#         InlineKeyboardButton(text='➡️', callback_data=f'{_product["id"] + 1}')
#     ])
#     ikm.row(InlineKeyboardButton(text='Savat (0) [1000] narxi', callback_data='123'))
#     caption = f'{_product["caption"]} \n <b>({_product["price"]})</b>'
#     await message.answer_photo(URLInputFile(_product['image']), caption, ParseMode.HTML, reply_markup=ikm.as_markup())
#
#
# @dp.callback_query()
# async def call_handler(callback: CallbackQuery) -> None:
#     if callback.data.isdigit():
#         _id = int(callback.data)
#         if 1 <= _id <= len(products):
#             for _product in products:
#                 if _product['id'] == _id:
#                     break
#             else:
#                 await callback.answer('Xato', show_alert=True)
#             ikm = InlineKeyboardBuilder()
#             ikm.row(*[
#                 InlineKeyboardButton(text='⬅️', callback_data=f'{_product["id"] - 1}'),
#                 InlineKeyboardButton(text='➕', callback_data=f'plus_{_product["price"]}'),
#                 InlineKeyboardButton(text='➡️', callback_data=f'{_product["id"] + 1}')
#             ])
#             ikm.row(InlineKeyboardButton(text='Savat (0) [1000] narxi', callback_data='123'))
#             caption = f'{_product["caption"]} \n <b>({_product["price"]})</b>'
#             photo = InputMediaPhoto(type=InputMediaType.PHOTO, media=URLInputFile(_product['image']), caption=caption,
#                                     parse_mode=ParseMode.HTML)
#             await callback.message.edit_media(photo, callback.inline_message_id, reply_markup=ikm.as_markup())
#         else:
#             await callback.answer('Xato', show_alert=True)
#     elif callback.data.startswith('plus'):
#         _id1 = callback.data.split('_')[-1]
#         s = ''
#         s += _id1
#
#
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

#######################################################################################################################
# bot
#######################################################################################################################

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
# info = RedisDict()
#
#
# @dp.message(CommandStart())
# async def informations(message: Message):
#     rkm = ReplyKeyboardBuilder()
#     user = message.from_user
#     info[str(user.id)] = {
#         'first_name': user.first_name,
#         'last_name': user.last_name,
#         'username': user.username
#     }
#     rkm.add(KeyboardButton(text="Nomer yuborish", request_contact=True))
#     await message.answer(text="Nomeringizni yuboring", reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.message(F.content_type.in_({ContentType.CONTACT}))
# async def contacts(message: Message):
#     l = info.get(str(message.from_user.id))
#     l['phone'] = message.contact.phone_number
#     info.update({str(message.from_user.id): l})
#     rkm = ReplyKeyboardBuilder()
#     rkm.add(KeyboardButton(text="Lokatsiya yuborish", request_location=True))
#     await message.answer(text="Lokatsiyangizni yuboring", reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.message(F.content_type.in_({ContentType.LOCATION}))
# async def location(message: Message):
#     l = info.get(str(message.from_user.id))
#     l['address'] = {
#         'longitude': message.location.longitude,
#         'latitude': message.location.latitude
#     }
#     info.update({str(message.from_user.id): l})
#
#     await message.answer("Malumotlaringiz muvoffaqiyatli saqlandi")
#
#
# @dp.message(F.text == '/admin')
# async def admin(message: Message):
#     msg = 'Users:\n'
#     for i, user in enumerate(info, start=1):
#         msg += f'{i}. <b>{user}</b>\n'
#         user = info.get(user)
#         msg += f'   {user["first_name"]} {user["last_name"]}\n'
#         msg += f'   {user["phone"]}\n'
#         msg += f'   {user["username"]}\n'
#         msg += f'   {user["address"]["latitude"]} {user["address"]["longitude"]} \n\n'
#     await message.answer(msg, parse_mode="HTML")
#
#
# async def main() -> None:
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())



########################################################################################################################
#bot
########################################################################################################################
#
# import asyncio
# import json
# import logging
# import smtplib
# import ssl
# import sys
#
# from aiogram import Bot, Dispatcher, F
# from aiogram.enums import ParseMode, InputMediaType, ContentType
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.methods import edit_message_reply_markup
# from aiogram.types import Message, KeyboardButton, URLInputFile, InlineKeyboardButton, CallbackQuery, \
#     ReplyKeyboardRemove, InputMediaPhoto, InputFile
# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
# from redis_dict import RedisDict
#
# TOKEN = '6333492425:AAEPhavOYXmAEon43siELnx9iBijHFAjBFs'
# dp = Dispatcher()
# Admin = 5736483354
# info = RedisDict()
#
# @dp.message(CommandStart())
# async def informations(message: Message):
#     user = message.from_user
#     info[str(user.id)] = {
#         'first_name': user.first_name,
#         'last_name': user.last_name,
#         'username': user.username
#     }
#     rkm = ReplyKeyboardBuilder()
#     rkm.add(KeyboardButton(text="nomer yuborish", request_contact=True))
#     await message.answer("Nomeringizni yuboring")
#
#
# @dp.message(F.content_type.in_({ContentType.CONTACT}))
# async def contacts(message: Message):
#     l = info.get(str(message.from_user.id))
#     l['phone'] = message.contact.phone_number
#     info.update({str(message.from_user.id): l})
#     rkm = ReplyKeyboardBuilder()
#     rkm.add(KeyboardButton(text='Lokatsiya yuborish', request_location=True))
#     await message.answer("Lokatsiyangizni yuboring")
#
#
# @dp.message(F.content_type.in_({ContentType.LOCATION}))
# async def locations(message: Message):
#     l = info.get(str(message.from_user.id))
#     l['address'] = {
#         'longitude': message.location.longitude,
#         'latitude': message.location.latitude
#     }
#     info.update({str(message.from_user.id): l})
#
#
# @dp.message(F.text == '/admin')
# async def admins(message:Message):
#     msg = 'Users:\n'
#     for i, user in enumerate(info, 1):
#         msg += f'{i}. <b>{user}</b>\n'
#         user = info.get(user)
#         msg += f'   {user["first_name"]} {user["last_name"]}\n'
#         msg += f'   {user["phone"]}\n'
#         msg += f'   {user["username"]}\n'
#         msg += f'   {user["address"]["latitude"]} {user["address"]["longitude"]} \n\n'
#     await message.answer(msg, parse_mode="HTML")
#
#
#
# async def main() -> None:
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())
