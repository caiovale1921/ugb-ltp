import sqlite3
from sqlite3.dbapi2 import Cursor, connect

connection = sqlite3.connect('Cliente.db')
db = connection.cursor()

nome = 'Caio'
idade = 18

sql = '''INSERT INTO Clientes (nome, idade) VALUES (?, ?);'''

db.execute(sql, (nome, idade))
connection.commit()
print('Gravado')
connection.close()