class Aluno:

    def __init__(self, nome = None, notas = None): # Método construtor
        self.Nome = nome
        self.Notas = notas

    def GetAlunosWithSixNotesOrMore(self): #Método para pegar os alunos com a quantidade de notas maior que 6
        file = open('notasEstudantes.txt', 'r')
        result = []

        for i in range(len(file.readlines())):
            file.seek(0 , 0)
            line = file.readlines()[i].replace('\n', '').split(' ')
            self.Nome = line[0]
            self.Notas = line[1:]
            if (len(self.Notas) > 6):
                result.append(f'{self.Nome}')

        file.close()   

        return result

    def GetMedia(self): # Método para pegar a média das notas dos alunos
        file = open('notasEstudantes.txt', 'r')
        result = []

        for i in range(len(file.readlines())):
            file.seek(0 , 0)
            line = file.readlines()[i].replace('\n', '').split(' ')
            self.Nome = line[0]
            notasAux = line[1:]
            self.Notas = [float(val) for val in notasAux]
            result.append(f'{self.Nome} : {sum(self.Notas) / len(self.Notas):.2f}')

        file.close()
        
        return result

    def GetMinAndMax(self): #Método para pegar a menor e maior nota do aluno.
        file = open('notasEstudantes.txt', 'r')
        result = []

        for i in range(len(file.readlines())):
            file.seek(0 , 0)
            line = file.readlines()[i].replace('\n', '').split(' ')
            self.Nome = line[0]
            notasAux = line[1:]
            self.Notas = [float(val) for val in notasAux]
            result.append(f'{self.Nome} : Min:{min(self.Notas)} Max:{max(self.Notas)}')

        file.close()
        
        return result

    
