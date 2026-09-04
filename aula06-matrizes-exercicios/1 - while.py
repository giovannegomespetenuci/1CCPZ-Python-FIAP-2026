continuar = True
while continuar:
    print("Olá, mundo!")
    check = int(input("Deseja continuar? Digite 1 para Sim e 0 para Não: "))
    while check not in [0,1]:
        print("Opção inválida!")
        check = int(input("Deseja continuar? Digite 1 para Sim e 0 para Não: "))
    if check == 0:
        print("Até a próxima!")
        continuar = False
    else:
        continuar = True