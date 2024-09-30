import os

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import keyboards.inline_keyboards as kb

from states.create_document import CreateNote, document, CreateDocument
from utils.delete_files import delete_files_in_folder
from utils.save_document import save_document
from db.users import get_user_id_by_username
from db.documents import create_document

router = Router()

@router.callback_query(F.data == 'create_note')
async def create_note(callback: CallbackQuery):
    await callback.message.answer('Отправьте фото, voice или текст ✍️',
                                  reply_markup=kb.create_note)


@router.callback_query(F.data == 'get_document')
async def get_document(callback: CallbackQuery):
    await callback.message.answer('Идет сборка документа...')

    file, document_name = save_document()
    await callback.message.answer_document(file)

    await callback.message.answer('Выберите действие',
                                  reply_markup=kb.action_with_document)


@router.callback_query(F.data == 'send_photo')
async def send_photo(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CreateNote.photo)
    await callback.message.answer(text='Отправьте фото')


@router.callback_query(F.data == 'send_voice')
async def send_voice(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CreateNote.voice)
    await callback.message.answer(text='Отправьте войс')


@router.callback_query(F.data == 'send_text')
async def send_text(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CreateNote.text)
    await callback.message.answer(text='Отправьте текст')


@router.callback_query(F.data == 'finish_note')
async def finish_note(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Хотите закончить документ?',
                                  reply_markup=kb.action_with_document)
    await state.clear()
    if os.path.exists('downloads/photo') or os.path.exists('downloads/voices'):
        delete_files_in_folder('downloads/photo')
        delete_files_in_folder('downloads/voices')


@router.callback_query(F.data == 'finished')
async def finished(callback: CallbackQuery, state: FSMContext):
    username = callback.from_user.username

    user_id = await get_user_id_by_username(username)

    if user_id is None:
        await callback.message.answer("Ошибка: пользователь не найден в базе данных.")
        return

    file, document_name = save_document()
    await callback.message.answer_document(file)

    await callback.message.answer('Сессия завершена')
    await state.clear()

    if os.path.exists('downloads/photo') or os.path.exists('downloads/voices'):
        delete_files_in_folder('downloads/photo')
        delete_files_in_folder('downloads/voices')

    await create_document(user_id=user_id, file_path=f'documents/{document_name}')
