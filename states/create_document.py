from aiogram.fsm.state import StatesGroup, State

from docx import Document

document = Document()

class CreateDocument(StatesGroup):
    document_name = State()


class CreateNote(StatesGroup):
    photo = State()
    voice = State()
    text = State()