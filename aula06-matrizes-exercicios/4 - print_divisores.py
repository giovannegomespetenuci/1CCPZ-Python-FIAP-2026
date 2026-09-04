n = int(input("Digite um número inteiro positivo: "))
while n < 0:
    print("Número inválido. Digite apenas valores positivos")
    n = int(input("Digite um número inteiro positivo: "))

divisores = []
for i in range(1, n+1):
    if n % i == 0:
        divisores.append(i)

print(f"Os divisores de {n} são: {divisores}")