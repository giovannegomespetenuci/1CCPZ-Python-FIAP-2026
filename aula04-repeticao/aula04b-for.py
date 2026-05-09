for count_music in range(3):
    print(f"música {count_music}")

# de 1 até 11, pulando de 2 em 2
for i in range (1, 12, 2):
    print(i)

#ATIVIDADE 3
qtd_music = int(input("Digite a quantidade de músicas que você tem na playlist: "))

for i in range(qtd_music):
    print(f"Música {i}")


# LAÇOS ANINHADOS
# REP. ENCADEADA
for i in range(0, 4):
    for j in range (0,3,2):
        print(f"i:{i}, j:{j}")