import sqlite3
import os

def add_product(genre: str):
    try:
        database_path = 'diplom_database.db'
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        price = 0
        g_id = 0

        if conn:
            directory = f'D:/diplom_kartigo/diplom_kartigo/backend/src/music/genres/{genre}/'
            all_entries = os.listdir(directory)
            wav_files = [entry for entry in all_entries if os.path.isfile(os.path.join(directory, entry))]

            for wav in wav_files:
                if genre == 'Lyrical':
                    price = 19.99
                    g_id = 2
                if genre == 'Reggaeton':
                    price = 29.99
                    g_id = 3
                if genre == 'Rock':
                    price = 14.99
                    g_id = 4
                if genre == 'Trap':
                    price = 34.99
                    g_id = 5

                cursor.execute('''
                    INSERT INTO products (data_name, description, price, genre_id)
                    VALUES (?, ?, ?, ?)
                    ''', (wav, 'Описание', price, g_id))
                print(wav)
            conn.commit()
        else:
            conn.rollback()
        print("YES!!")
    except Exception as e:
        print("ERRORRRR:", e)


add_product('Trap')