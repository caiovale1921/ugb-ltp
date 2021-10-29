# Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo.
# A função deve retornar um valor booleano.

def isPositivo(numero):
    if (numero > 0):
        return True
    return False

while True:
    numero = int(input("Insira um numero inteiro:"))
    if isPositivo(numero) is True:
        print ("Numero Positivo")
    else:
        print ("Numero Negativo")