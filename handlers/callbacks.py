from aiogram import Router, F
from aiogram.types import FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext

import keyboards.inline_keyboards as kb

from states.create_document import CreateNote, document


router = Router()

@router.callback_query(F.data == 'create_note')
async def create_note(callback: CallbackQuery):
    await callback.message.answer('Отправьте фото, voice или текст',
                                  reply_markup=kb.create_note)


@router.callback_query(F.data == 'send_photo')
async def send_photo(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CreateNote.photo)
    await callback.message.answer(text='Отправьте фото')


@router.callback_query(F.data == 'send_voice')
async def send_voice(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CreateNote.voice)
    await callback.message.answer(text='Отправьте войс')


@router.callback_query(F.data == 'get_document')
async def get_document(callback: CallbackQuery):
    await callback.message.answer('Идет сборка документа...')

    document.save('document.docx')
    file = FSInputFile('document.docx')
    await callback.message.answer_document(file)
    await callback.message.answer('Выберите действие',
                                  reply_markup=kb.action_with_finished_document)


@router.callback_query(F.data == 'finish_note')
async def finish_note(callback: CallbackQuery):
    await callback.message.answer('Хотите закончить документ?',
                                  reply_markup=kb.action_with_document)


@router.callback_query(F.data == 'finished')
async def finished(callback: CallbackQuery):
    await callback.message.answer('Сессия завершена')