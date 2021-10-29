import sqlite3
from sqlite3.dbapi2 import Cursor, connect

connection = sqlite3.connect('Cliente.db')
db = connection.cursor()

sql = "DELETE FROM Clientes WHERE id = ?;"

id = 1
db.execute(sql, (1,))
connection.commit()
print('Deletado')
connection.close()