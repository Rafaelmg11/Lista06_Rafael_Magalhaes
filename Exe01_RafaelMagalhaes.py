#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja,
# posição na lista) desse item na tupla.

paises = ('Brasil','Chile','Canada','Venezuela','Italia')

print("Paises: ",paises)

resposta = (input("Insira um dos paises: "))

try:
    i = paises.index(resposta)

    print("O indice de {} é: {}".format(resposta,i))
except:
    
    while resposta not in paises:
        print("Pais inserido invalido!")
        print("Tente Novamente!\n")
        print("Paises: ",paises)
        resposta = (input("Insira um dos paises: "))
    
    i = paises.index(resposta)


    print("O indice de {} é: {}".format(resposta,i))

print("Rafael de Almeida de Magalhaes")   
print("Encerrando o Programa...")