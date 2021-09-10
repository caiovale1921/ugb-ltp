'''
Construa um algoritmo de votação para a Prefeitura Municipal de Volta
Redonda. Os votos serão computados da seguinte maneira:

-1 - sair
0 - branco
1 - Samuca
2 - Neto
3 - Baltazar
>=4 - Nulo

A saída deverá ser:
+ O número do candidato vencedor
+ O número de votos em branco
+ O número de votos nulos
+ o número de eleitores

'''
def getPrefeitoByVotos(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return "Samuca" #n1
    elif n2 > n3:
        return "Neto" #n2
    else:
        return "Baltazar" #n3

votosBranco   = 0
votosSamuca   = 0
votosNeto     = 0
votosBaltazar = 0
votosNulo     = 0
voto          = 0
eleitores     = 0

while True:
    voto = int(input("Insira o numero do candidato: "))

    if voto == -1:
        break
    
    eleitores += 1

    if voto == 0: #Branco
        votosBranco += 1
    elif voto == 1: #Samuca
        votosSamuca += 1
    elif voto == 2: #Neto
        votosNeto += 1
    elif voto == 3: #Baltazar
        votosBaltazar += 1
    elif voto >= 4: #Nulo
        votosNulo += 1
    else:
        print("Invalido, insira novamente")
        eleitores -= 1

print("-------Resultado-------\nMais votado:", getPrefeitoByVotos(votosSamuca, votosBaltazar, votosNeto),
"\nVotos em branco:", votosBranco,
"\nVotos nulos:", votosNulo,
"\nTotal de eleitores:",eleitores)