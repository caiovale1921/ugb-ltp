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