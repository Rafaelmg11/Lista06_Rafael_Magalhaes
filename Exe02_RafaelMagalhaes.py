#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos,
# solicite ao usuário para digitar um nome de produto e exiba a posição dele, em seguida peça para 
# digitar numero entre 0 e 9 e exiba o produto da tupla.

# Uma tupla é imutuavel entao vou adicionar a uma LISTA 

produtosLista = []


for i in range(10):
    produto = (input("Insira um produto: "))

    produto = produto.lower()

    produtosLista.append(produto)
    indiceLista = produtosLista.index(produto)
    print("O indice de {} é : {}".format(produto,indiceLista))

#DECLARANDO UMA TUPLA ADICIONANDO A LISTA NA TUPLA
produtosTupla = tuple(produtosLista)

print("Produtos: ",produtosTupla)

indiceTupla = int (input("Digite um número de 0 á 9: "))

if indiceTupla <10 :
    print("Produto:{}".format(produtosTupla[indiceTupla]))

else:
    print("Produto Invalido!")
    print("Encerrando o programa...")

print("Rafael de Almeida de Magalhaes")   
print("Encerrando o Programa...")