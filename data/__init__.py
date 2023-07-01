import mysql.connector as connector
import os

# change venv variables when uploading to the server .
connection = connector.connect(host=os.environ['HOST'], user=os.environ['USER'], password=os.environ['PASSWORD'], db=os.environ['DB'])
cursor = connection.cursor(buffered=True)


cursor.execute('''CREATE TABLE IF NOT EXISTS market(
    user_id INT UNIQUE,
    tickers TEXT);''')
connection.commit()