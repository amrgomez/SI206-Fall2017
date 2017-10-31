import sqlite3

conn= sqlite3.connect('ages.sqlite')
cur= conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

cur.execute('DELETE FROM Ages;')
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Umut', 31))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Aurea', 40))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Eamon', 32))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Harman', 22))

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

conn.commit()
for row in cur:
    print(row)
    break

cur.close()
conn.close()
