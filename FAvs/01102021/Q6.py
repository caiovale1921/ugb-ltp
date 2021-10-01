'''
Questão 06 (1.5 ponto): Construir um algoritmo capaz de ler um número
e imprimir se este número é par ou ímpar
'''
numero = float(input("Insira um numero: "))

if((numero % 2) == 0):
    print("Numero par")
else:
    print("Numero Impar")