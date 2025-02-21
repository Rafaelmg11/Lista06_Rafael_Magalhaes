#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos,
# solicite ao usuário para digitar um nome de produto e exiba a posição dele, em seguida peça para 
# digitar numero entre 0 e 9 e exiba o produto da tupla.

# Uma tupla é imutuavel entao vou adicionar a uma LISTA 

produtosLista = []


for i in range(4):
    produto = (input("Insira um produto: "))

    produto = produto.lower()

    produtosLista.append(produto)
    indiceLista = produtosLista.index(produto)
    print("O indice desse de {} é : {}".format(produto,indiceLista))

#DECLARANDO UMA DUPLA ADICIONANDO A LISTA NA TUPLA
produtosTupla = tuple(produtosLista)

print("Produtos: ",produtosTupla)

indiceTupla = (input("Digite um número de 0 á 9: "))

try:
    print("Produto:{}".format(produtosTupla(indiceTupla)))

except:
    while indiceTupla not in produtosTupla(indiceTupla):
        print("Esse produto não existe!")
        print("Tente Novamete!\n")
        indiceTupla = (input("Digite um número de 0 á 9: "))
    print("Produto:{}".format(produtosTupla(indiceTupla)))
