'''
Criar um algoritmo capaz de calcular o faturamento de uma lista de
produtos com suas respectivas quantidades e preço.
Verifique a entrada dos produtos, ao digitar sair a captação se encerra.
Calcular o faturamento com a equação:
faturamento = faturamento + (quantidade * preço)
Utilize uma estrutura for para percorrer toda a lista e pegar as variáveis
quantidade e preço
'''
class Produto():
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        
def isSair(text):
    if text == "Sair" or text == "sair":
        return True
    return False

produtos = list()
faturamento = 0

while True:
    inputProdutoNome = input("Insira o nome do produto: ")
    if isSair(inputProdutoNome):
        break
    inputProdutoQuantidade = input("Insira a quantidade do produto: ")
    if isSair(inputProdutoQuantidade):
        break
    inputProdutoPreco = input("Insira o preço do produto: ")
    if isSair(inputProdutoPreco):
        break

    try:
        produtos.append(Produto(inputProdutoNome, float(inputProdutoQuantidade), float(inputProdutoPreco)))
        print("Gravado com sucesso\n")
    except:
        print("Ocorreu um erro na gravação, insira o produto novamente")

for produto in produtos:
    faturamento += (produto.quantidade * produto.preco)

print("=======Faturamento=======\nFaturmanto: R$", faturamento)