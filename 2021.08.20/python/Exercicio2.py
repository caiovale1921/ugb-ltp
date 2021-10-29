# EXERCICO 2 - MEDIA DE UMA LISTA DE INTEIROS
valores = [] # DECLARAÇÃO DA LISTA

n = 0 # INICIALIZAÇÃO DO CONTADOR

# ESTRUTURA DE REPETIÇÃO DINAMICA (VAI ISERINDO VALORES ATÉ DIGITAR -1)
while True:
    n = int(input("Insira um numero: "))
    if n < 0:
        break
    else:
        valores.append(n)
'''
### ESSE TRECHO AQUI, FAZ A FUNÇÃO DO SUM - ELE VAI PEGANDO OS ELEMENTOS E SOMANDO EM UMA VARIAVEL
valoresTotal = 0
for i in range(0, len(valores)):
    valoresTotal += valores[i]
    i += 1
'''

# FAZ A MEDIA DOS VALORES DA LISTA
print ("Lista: ", valores, "\nMédia: ", (sum(valores)) / (len(valores)))