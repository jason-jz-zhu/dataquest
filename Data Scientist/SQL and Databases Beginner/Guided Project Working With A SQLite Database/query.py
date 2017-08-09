import sqlite3

conn = sqlite3.connect('factbook.db')

cursor = conn.cursor()
query = 'SELECT * FROM facts ORDER BY population LIMIT 10'

print(cursor.execute(query).fetchall())

data