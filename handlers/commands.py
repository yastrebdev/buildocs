from aiogram import html, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.create_document import CreateDocument

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")


@router.message(Command('newdoc'))
async def create_document(message: Message, state: FSMContext):
    await state.set_state(CreateDocument.document_name)
    await message.answer(text='Введите название документа')