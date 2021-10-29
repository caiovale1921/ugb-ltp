# Faça uma função que recebe a média final de um aluno por parâmetroe retorna o seu conceito,
# conforme a tabela abaixo:

# de 0,0 a 4,9    -> D
# de 5,0 a 6,9    -> C
# de 7,0 a 8,9    -> B
# de 9,0 a 10,0   -> A

def getMedia(nota: float):
    if (nota >= 0 and nota <= 4.9):
        return "D"
    elif (nota <= 6.9):
        return "C"
    elif (nota <= 8.9):
        return "B"
    elif (nota <= 10):
        return "A"
    else:
        return "Nota Invalida"

while True:
    nota = float(input("Insira a média final do aluno:"))
    print ("Média do aluno: " + (getMedia(nota)))