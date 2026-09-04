n = int(input("Digite um número inteiro positivo: "))
while n < 0:
    print("Número inválido. Digite apenas valores positivos")
    n = int(input("Digite um número inteiro positivo: "))

soma = 0
for i in range(1, n+1):
    soma += i

print(f"A soma dos números inteiros 1 e {n} é {soma}")