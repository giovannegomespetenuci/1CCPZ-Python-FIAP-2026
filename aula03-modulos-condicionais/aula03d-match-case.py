# imagine um sistema que recolha a escolha do usuário
# escolha_usuario
# caso 0: sair do programa
# caso 1: entrar no programa
# else: erro

escolha_usuario = 1
match escolha_usuario:
    case 0:
        print("Saindo do programa")
    case 1:
        print("Entrando no programa")
    case _:
        print("Erro!")