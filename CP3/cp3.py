temps = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

#definição de variáveis e contadores
somatemps = 0
mediatemps = 0
contsala = 0
critico = 33
registrocrit = 0
contadorcrit = 0
salacrit = 0

#percorre o vetor inteiro
for temp in temps:
    for coisa in temp:
        somatemps += coisa #soma as temps de uma sala
        if coisa >= 33:
            registrocrit += 1 #adiciona mais um no contador de registro crítico caso a temperatura analisada seja maior ou igual a 33
    mediatemps = somatemps/len(temps) #calcula a média após percorrer as temperaturas de uma sala
    contsala += 1 #contador que registra o número da sala percorrida

    print(f"Relatório sala {contsala}")
    print(f"Média de temperatura: {mediatemps}")
    print(f"Registros críticos: {registrocrit}")

    while registrocrit > 0 and registrocrit > contadorcrit:
        #loop while que sempre mantém atualizado a sala com maior risco, ou seja, maior quantidade de registros críticos
        contadorcrit = registrocrit
        salacrit = contsala

    #zera algumas variáveis para registrar o valor da próxima percorrida
    mediatemps = 0
    somatemps = 0
    registrocrit = 0
    print()

print(f"Sala com maior risco: {salacrit}") #print fora dos laços for para que o resultado exposto seja o final