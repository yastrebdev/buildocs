from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

action_with_document = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать заметку', callback_data='create_note')],
    [InlineKeyboardButton(text='Получить документ', callback_data='get_document')],
    [InlineKeyboardButton(text='Закончить', callback_data='finished')],
])


create_note = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отправить фото', callback_data='send_photo')],
    [InlineKeyboardButton(text='Отправить voice', callback_data='send_voice')],
    [InlineKeyboardButton(text='Отправить текст', callback_data='send_text')],
    [InlineKeyboardButton(text='Закончить заметку', callback_data='finish_note')],
])