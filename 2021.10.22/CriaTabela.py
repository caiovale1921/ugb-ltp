import sqlite3
from sqlite3.dbapi2 import Cursor, connect

#Criando e abrindo conexão com o DB
connection = sqlite3.connect('Cliente.db')
db = connection.cursor()

try:
#Comando sql para criando a tabela de clientes
    sql = """
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, idade INTEGER
        );
    """

    db.execute(sql)
    print("Tabela criada!")
except:
    print('Problemas ao criar a tabela')
