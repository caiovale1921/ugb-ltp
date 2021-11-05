'''
Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, retornar valor do Lado e calcular Área;
'''

class Quadrado:

    def __init__(self, tamanho: None):
        self.Tamanho = tamanho

    def MudaValor(self, novoTamanho):
        self.Tamanho = novoTamanho
    
    def GetValor(self):
        return self.Tamanho

    def CalcArea(self):
        return self.Tamanho ** 2