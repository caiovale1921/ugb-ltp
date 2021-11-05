'''
Classe Retangulo: Crie uma classe que modele um retângulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e
Altura, a escolher)
b. Métodos: Mudar valor dos lados, retornar valor dos lados,
calcular Área e calcular Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao
usuário que informe as medidas de um local. Depois, deve criar
um objeto com as medidas e calcular a quantidade de pisos e de
rodapés necessárias para o local.
'''

class Retangulo:

    def __init__(self, comprimento = None, largura = None):
        self.Comprimento = comprimento
        self.Largura = largura

    def ChangeValues(self, comprimento, largura):
        self.Comprimento = comprimento
        self.Largura = largura

    def GetValues(self):
        resultList = []
        resultList.append(self.Comprimento)
        resultList.append(self.Largura)
        return resultList
    
    def CalcArea(self):
        return float(self.Comprimento * self.Largura)

    def CalcPerimetro(self):
        return float(2 * (self.Comprimento + self.Largura))
    

retangulo = Retangulo()

retangulo.Largura = input("Insira a Largura")
retangulo.Comprimento = input("Insira o Comprimento")