import pyrebase

class Aluno:

    def __init__(self, nome = None, disciplina = None, idade = 0):
        self.Nome = nome
        self.Disciplina = disciplina
        self.Idade = idade

DbConf = {
    "apiKey": "AIzaSyBqLBA8kfIKCjcv-h6lRHIMylQxBsStNBE",
    "authDomain": "clientes-28e4a.firebaseapp.com",
    "databaseURL": "https://clientes-28e4a.firebaseio.com",
    "storageBucket": "clientes-28e4a.appspot.com"
    }

firebaseDb = pyrebase.pyrebase.initialize_app(DbConf)

db = firebaseDb.database()

aluno = Aluno('Caio Victor F. de Souza Vale', 'Programação I', 19)

data = {
    'name': aluno.Nome,
    'disciplina': aluno.Disciplina,
    'idade': aluno.Idade
}

db.child('segundo-periodo').child('2021101022').set(data)