# Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo.
# A função deve retornar um valor booleano.

def isPositive(i):
    if (i > 0):
        return True
    return False

while True:
    number = int(input("Insert a integer number:"))
    if isPositive(number) is True:
        print ("Positive Number")
    else:
        print ("Negative Number")