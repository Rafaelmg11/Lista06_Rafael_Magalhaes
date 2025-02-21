#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos,
# solicite ao usuário para digitar um nome de produto e exiba a posição dele, em seguida peça para 
# digitar numero entre 0 e 9 e exiba o produto da tupla.

# Uma tupla é imutuavel entao vou adicionar a uma LISTA 

produtosLista = []

for i in range(10):
    produtosLista.append(input("Insira um produto: "))

#DECLARANDO UMA DUPLA ADICIONANDO A LISTA NA TUPLA
produtosTupla = tuple(produtosLista)

print("Produtos: ",produtosTupla)


