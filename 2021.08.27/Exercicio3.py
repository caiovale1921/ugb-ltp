# Faça um procedimento que recebe a idade de um nadador por parâmetro e retorna,
# também por parâmetro, a categoria desse nadador de acordo com a tabela
# 5 a 7 anos                     -> Infantil A
# 8 a 10 anos                    -> Infantil B
# 11-13 anos                     -> Juvenil A
# 14-17 anos                     -> Juvenil B
# Maiores de 18 anos (inclusive) -> Adulto

# Utilizando if else
def getCategoriaForIdadeByIfElse(idade):
    if (idade >= 5 and idade <= 7):
        return "Infantil A"
    elif (idade >= 8 and idade <= 10):
        return "Infantil B"
    elif (idade >= 11 and idade <= 13):
        return "Juvenil A"
    elif (idade >= 14 and idade <= 17):
        return "Juvenil B"
    else:
        return "Adulto"

'''
Exemplo de implementação    

print (getCategoriaForIdadeByIfElse(16))

'''

# Utilizando switch-case
def getCategoriaForIdadeBySC(idade):
    switcher = {
        idade >= 5 and idade <= 7 : "Infantil A",
        idade >= 8 and idade <= 10 : "Infantil B",
        idade >= 11 and idade <= 13 : "Juvenil A",
        idade >= 14 and idade <= 17 : "Juvenil B"
    }

'''
Exemplo de implementação    

print switcher.get(idade, "Adulto")

'''