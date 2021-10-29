from typing import Counter


class MyCrud:

    def __init__(self, banco = None):
        import sqlite3
        self.connection = sqlite3.connect(banco)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.connection.close()
        print('Connection Closed')

    def createTable(self):
        sql = """
                CREATE TABLE IF NOT EXISTS Clientes(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER
                );
              """
        self.cursor.execute(sql)
        print('Table created')

    def getAllClientes(self):
        sql = """
                select * from clientes;
              """
        result = self.cursor.execute(sql)
        return result.fetchall()

    def insert(self, nome = "SEM NOME", idade = "0"):
        try:
            sql = """
                    INSERT INTO Clientes (nome, idade) VALUES (?, ?);
                """
            self.cursor.execute(sql)
            print("Inserted")
        except:
            print("Erro to Insert")