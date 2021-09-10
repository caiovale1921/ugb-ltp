'''
Construa um algoritmo capaz de permitir a entrada, via teclado, do nome
do aluno e suas duas notas até que o nome sair aparecer e terminar o
programa. No final deverá apresentar o nome e a média das notas junto com
mensagem aprovado (>=7) ou reprovado (<7).
'''
nomeAluno = input(print("Insira o nome do aluno:"))
notasAluno = []
i = 1
while True:
    notaAlunoInsert = input(print("Insira a nota ", i ,"do aluno"))
    if notaAlunoInsert == "sair":
        break
    notasAluno.append(float(notaAlunoInsert))
    i += 1

media = (sum(notasAluno)) / (len(notasAluno))
print ("Notas: ", notasAluno, "\nMédia: ", media)
if media <= 7:
    print ("Aluno: ", nomeAluno," -> Reprovado")
else:
    print ("Aluno: ", nomeAluno," -> Aprovado")