import os
from datetime import datetime
from aiogram.types import FSInputFile
from states.create_document import document


def save_document():
    cur_time = datetime.now().strftime('%d_%m_%Y_%H_%M')
    document_name = f'{cur_time}.docx'

    if not os.path.exists('documents'):
        os.mkdir('documents')

    document.save(f'documents/{document_name}')
    file = FSInputFile(f'documents/{document_name}')

    return file, document_name