from aiogram import html, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from db.users import create_user, find_user_by_username
from states.create_document import CreateDocument

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    username = message.from_user.username
    name = message.from_user.first_name

    await message.answer(f"Привет, {html.bold(message.from_user.first_name)}! 👋\n\n"
                         "Это бета версия бота, будьте терпимей\n\n"
                         "Начать работу -- /newdoc\n"
                         "Как пользоваться -- /about\n\n"
                         f"Баги {html.bold('/')} комментарии {html.bold('/')} предложения - @yastrebbov")

    user = await find_user_by_username(username)

    if not user:
        await create_user(username, name)


@router.message(Command('about'))
async def help_me(message: Message):
    await message.answer(text='Помогли как смогли (раздел в разработке)...')


@router.message(Command('newdoc'))
async def create_document(message: Message, state: FSMContext):
    await state.set_state(CreateDocument.document_name)
    await message.answer(text='Введите название документа ✏️')