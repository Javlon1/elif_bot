from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_delete = KeyboardButton('/delete')

kb_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('/menu_176235000'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)