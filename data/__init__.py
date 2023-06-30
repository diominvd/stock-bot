import sqlite3


connection = sqlite3.connect('data/database.db')
cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS market(
    user_id INTEGER UNIQUE,
    tickers TEXT)''')
connection.commit()