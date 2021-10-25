import sqlite3
from sqlite3.dbapi2 import Cursor, connect

connection = sqlite3.connect('Cliente.db')
db = connection.cursor()

nome = 'Caio'
idade = 19

sql = "UPDATE Clientes Set nome = ?, idade = ?;"

db.execute(sql, (nome, idade))
connection.commit()
print('Editado')
connection.close()