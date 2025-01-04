import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', (i*10), 1000))

"""for id in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, id))"""

cursor.execute('''
UPDATE Users
SET balance = 500
WHERE rowid % 2 = 1
''')

cursor.execute('''
DELETE FROM Users
WHERE rowid % 3 = 1
''')

cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

res = cursor.fetchall()

for i in res:
    print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}')


"""cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (32, 'John'))
cursor.execute("DELETE FROM Users WHERE username = ?", ('John',))
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    print(user)
cursor.execute("SELECT username, age FROM Users WHERE age > ?", (25,))
cursor.execute("SELECT username, age FROM Users GROUP BY AGE")
"""
connection.commit()
connection.close()
