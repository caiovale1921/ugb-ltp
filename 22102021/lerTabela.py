import sqlite3
from sqlite3.dbapi2 import Cursor, connect

connection = sqlite3.connect('Cliente.db')
db = connection.cursor()

sql = '''
      select * from Clientes
      '''

db.execute(sql)

print(db.fetchall())

connection.close()