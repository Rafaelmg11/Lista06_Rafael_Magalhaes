#EXE 003 - Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista.
#Depois de inserir os três nomes, pergunte se deseja adicionar outro. Se o fizer, permita que adicione mais nomes até responder "não".
#Quando ele responder "não", mostre quantas pessoas ele convidou para a festa, uma vez que o usuário tenha completado sua lista de nomes,
#exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista. Pergunte ao usuário se ele 
#ainda deseja que essa pessoa venha à festa. Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente.

nome = []
for i in range(3):
    nome.append (input("Digite um nome: "))

resposta = input("Você deseja convidar mais alguem para a festa? ")

resposta.lower()

while resposta == 'sim':
    nome.append (input("Digite um nome: "))
    resposta = input("Você deseja convidar mais alguem para a festa? ")

    resposta.lower()

i = len(nome)
print("Pessoas convidadas:",nome)
print("Foram convidadas {} pessoas".format(i))

nome2 = input("Digite um dos nomes da lista: ")

i = nome.index(nome2)

print("Posição na lista de conivados:",i)

resposta = input("Você deseja que {} ainda venha na festa? ".format(nome2))

if resposta == 'nao':

   nome.pop(i)

   print("Lista de convidados atualizada:",nome)

else:
    print("Boas Festas!")

print("Boas Festas!")
print("Rafael de Almeida de Magalhaes")   
print("Encerrando o Programa...")




    



