'''
Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: envelhecer, engordar, emagrecer, crescer. Obs: Por
padrão, a cada ano que nossa pessoa envelhece, sendo a idade
dela menor que 21 anos, ela deve crescer 0,5 cm.

'''

class Pessoa:

    def __init__(self, nome = None, idade = 0, peso = 0, altura = 0):
        self.Nome = nome
        self.Idade = idade
        self.Peso = peso
        self.Altura = altura

    def envelhecer(self):
        self.Idade += self.Idade
        if (self.Idade > 21):
            self.Altura += 0.5 

    def engordar(self, pesoGanho):
        self.Peso += pesoGanho

    def emagrecer(self, pesoPerdido):
        self.Peso -= pesoPerdido

    def crescer(self, alturaGanha):
        if (self.Idade < 21):
            self.Altura += alturaGanha