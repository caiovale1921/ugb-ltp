from Models import Aluno
import os # Usado para limpar o Console

def Clear(): # Método para limpar o console
        print("\n" * os.get_terminal_size().lines)

aluno = Aluno() #I nstanciando o aluno

while True: # Repetição para rodar o programa principal

    menu = str(input(
    '''\n
    Qual exercicio que execultar?
    1 - Alunos com mais de 6 notas
    2 - Média dos estudantes
    3 - Nota Minima e Maxima dos estudantes
    0 - Sair
    \n'''))

    if (menu == '0'):
        break
    
    elif (menu == '1'):

        Clear()
        print(f'Alunos com mais de 6 notas: {aluno.GetAlunosWithSixNotesOrMore()}')

    elif (menu == '2'):

        Clear()
        print(f'Média dos Alunos: {aluno.GetMedia()}')

    elif (menu == '3'):

        Clear()        
        print(f'Média dos Alunos: {aluno.GetMinAndMax()}')

    else:
        print('\nInsira um valor válido\n')


