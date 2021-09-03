# Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar.
# A função deve retornar um valor booleano.

def isPar(numero):
    if (numero % 2) == 0:
        return True
    return False

while True:
    numero = int(input("Insira um numero inteiro:"))
    if isPar(numero) is True:
        print ("Numero Par")
    else:
        print ("Numero Impar")