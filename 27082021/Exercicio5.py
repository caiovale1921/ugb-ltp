# Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar.
# A função deve retornar um valor booleano.

def isEven(i):
    if (i % 2) == 0:
        return True
    return False

while True:
    number = int(input("Insert a integer number:"))
    if isEven(number) is True:
        print ("Peer Number")
    else:
        print ("Odd Number")