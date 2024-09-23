from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

action_with_document = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать заметку', callback_data='create_note')],
    [InlineKeyboardButton(text='Получить документ', callback_data='get_document')],
])

action_with_finished_document = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Продолжить редактирование', callback_data='update_document')],
    [InlineKeyboardButton(text='Переименовать документ', callback_data='rename_document')],
    [InlineKeyboardButton(text='Закончить', callback_data='finished')],
])

create_note = InlineKeyboardMarkup(inline_keyboard=[
    # [InlineKeyboardButton(text='Отправить фото', callback_data='send_photo')],
    # [InlineKeyboardButton(text='Отправить voice', callback_data='send_voice')],
    # [InlineKeyboardButton(text='Отправить текст', callback_data='send_text')],
    [InlineKeyboardButton(text='Закончить заметку', callback_data='finish_note')],
])
