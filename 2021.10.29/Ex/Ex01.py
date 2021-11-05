'''
Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor
'''

class Bola:

    def __init__(this, cor = None, circunferencia = None, material = None):
        this.Cor = cor
        this.Circuferencia = circunferencia
        this.Material = material

    def trocaCor(this, novaCor):
        this.Cor = novaCor

    def mostraCor(this):
        return this.Cor