data = int(input("Insira seu ano de nascimento: "))
verif = 2026 - data
if verif < 16:
    print("Seu voto é é proibido")
elif verif < 18:
    print("Seu voto é opcional")
else:
    print("Seu voto é obrigatório")