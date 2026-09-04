def checkstatus(quantcerto, linha, colunas):
    if (quantcerto / colunas * 100) >= 80:
        print(f"Status de {endpoints[linha]}: Estável")
    else:
        print(f"Status de {endpoints[linha]}: Instável")

endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

linhas = len(status)
colunas = len(status[0])
certo = 0
erro = 0
erros = []
posicaoMaisErros = 0

for i in range(linhas):
    teve_erro_consecutivo = False
    for j in range(colunas):
        if 200 <= status[i][j] <= 299:
            certo += 1
        else:
            erro += 1
            if j > 0 and not (200 <= status[i][j-1] <= 299):
                teve_erro_consecutivo = True
    print(f"A porcentagem de requisições bem-sucedidas em {endpoints[i]} é de: {certo/colunas*100}%")
    if teve_erro_consecutivo:
        print(f"O endpoint {endpoints[i]} teve pelo menos dois erros consecutivos.")
        print(f"Status de {endpoints[i]}: Crítico")
    else:
        checkstatus(certo, i, colunas)
    erros.append(erro)
    certo = 0
    erro = 0
    print()
posicaoMaisErros = erros.index(max(erros))
print(f"O endpoint com mais erros é o {endpoints[posicaoMaisErros]}, com {erros[posicaoMaisErros]} erros")