# EXERCICIO 1 - DEFINIÇÃO DO TIPO DE UM TRIANGULO
while True:
    a = input("Insert number 1:")
    b = input("Insert number 2:")
    c = input("Insert number 3:")

    if (a == b and b == c):
        print("Triangulo equilatero")
    elif (a == b and b != c):
        print("Triangulo isoceles")
    else:
        print("Triangulo escaleno")