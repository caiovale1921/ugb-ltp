'''
Questão 04 (1.0 ponto): Escreva um algoritmo que leia três números inteiros e positivos (A, B, C)
e calcule a seguinte expressão e imprima o resultado de D:

D = (R+S)/2
Onde:
R = (A+B)**2
S = (B+C)**2

'''
a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))

r = (a + b)**2
s = (b + c)**2
d = (r + s)/2

print("O valor de D é:",d)