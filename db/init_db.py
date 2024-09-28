import sqlite3


def init_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        name TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Documents (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        file_path TEXT NOT NULL,
        upload_date TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    );
    ''')

    connection.close()


if __name__ == '__main__':
    init_db()