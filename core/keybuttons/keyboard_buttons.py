from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


search_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/search")]], resize_keyboard=True
)
cancel_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/cancel")]], resize_keyboard=True
)
