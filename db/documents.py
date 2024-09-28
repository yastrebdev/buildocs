import sqlite3
from datetime import datetime


async def create_document(*, user_id, file_path):
    upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection = sqlite3.connect('db/database.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Documents (user_id, file_path, upload_date) VALUES (?, ?, ?)',(user_id, file_path, upload_date))

    connection.commit()
    connection.close()