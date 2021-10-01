'''
Questão 07 (1.5 ponto): Construir um algoritmo capaz de ler um número
e imprimir se este número é positivo, negativo ou zero.
'''
numero = float(input("Insira um numero: "))

if(numero > 0):
    print("Numero Positivo")
elif(numero < 0):
    print("Numero Negativo")
else:
    print("Zero")