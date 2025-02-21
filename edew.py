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