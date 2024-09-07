import sqlite3

connection = sqlite3.connect('sqlite_mock.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS table1 
               (id INTEGER, col1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS table2 
               (id INTEGER, col2 TEXT)''')

cursor.executemany('INSERT INTO table1 (id, col1) VALUES (?, ?)', [
            (1, 'dummy'), (2, 'example'), (3, ''), (4, 'test')])
cursor.executemany('INSERT INTO table2 (id, col2) VALUES (?, ?)', [
            (1, 'value1'), (2, None), (3, 'value3'), (4, 'value4')])

# Commit the changes to the database
connection.commit()

# Query the database to retrieve data
cursor.execute('SELECT * FROM table1;')
rows = cursor.fetchall()
print(len(rows))
connection
connection.close()

