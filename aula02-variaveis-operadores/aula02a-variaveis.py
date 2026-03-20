print("olá mundo")
print(7+4)
print("7+4")
print("7" + "4") #concatenação de strings

#VARIÁVEIS

nome = "Jovas" #string
idade = 18 #int
peso = 90.2 #float
print(nome, idade, peso)
print(f"Oiii, {nome}!!!!") #formatação de print para inserir variáveis junto de uma string
print("Oiii, {nome}!!!!") #sem f

#INPUT - SIMULA UM FORMULÁRIO NO CMD
nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
print(nome, idade)
#print(idade+1) não vai printar pois input() armazena qualquer valor como string, até números
print(int(idade)+1) #ou nova_idade = int(idade)+1 e então print(nova_idade)
