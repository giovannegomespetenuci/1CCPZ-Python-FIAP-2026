cp = 0
while cp < 3:
    print(f"Produto {cp}")
    cp += 1

# while decrescente de 4 ate 1
i = 4
while i >= 4:
     print(i)
     i -= 1

# repetiçao com entrada od usuario
jogar = "Sim"

while jogar.lower() == "sim":
    print("Iniciar ou repetir o jogo")
    jogar = input("Deseja jogar novamente? ")



i = 0
while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
            break
    print(f"Produto {i}")