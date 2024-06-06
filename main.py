#!python
import sqlite3

conn = sqlite3.connect('Pos.db')
# conn = sqlite3.connect('example.db')

cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL
#     )
# ''')

# cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
# cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
# conn.commit()

# cursor.execute('SELECT * FROM users;')
# cursor.execute('SELECT * FROM pos')
# cursor.execute("PRAGMA database_list;")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# cursor.execute("SELECT * FROM android_metadata;")



rows = cursor.fetchall()

for row in rows:
    table_name = row[0]
    print("==START TABLE {table_name}==".format(table_name=table_name))
    # print("SELECT * FROM {table_name}".format(table_name=table_name))
    cursor.execute("SELECT * FROM {table_name}".format(table_name=table_name))
    for row in cursor.fetchall():
        print(row)

    print("==END TABLE {table_name}==".format(table_name=table_name))

cursor.close()
conn.close()
