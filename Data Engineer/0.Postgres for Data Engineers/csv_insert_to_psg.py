import csv
import psycopg2

with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    rows = [row for row in reader]

conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
for row in rows:
    cur.execute('INSERT INTO users VALUES (%s, %s, %s, %s)', row)

conn.commit()

cur.execute('SELECT * FROM users')
users = cur.fetchall()
conn.close()



########################################################################
### useing copy from function
########################################################################

conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
with open('user_accounts.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users', sep=',')

conn.commit()

cur.execute('SELECT * FROM users')
users = cur.fetchall()
conn.close()