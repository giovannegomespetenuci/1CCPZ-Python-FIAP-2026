import random

n = int(input("Digite a quantidade de números aleatórios que deseja: "))
while n < 0:
    print("Número inválido. Digite apenas valores positivos")
    n = int(input("Digite a quantidade de números aleatórios que deseja: "))

vetor_random = []
for i in range(1,n+1):
    a = random.randint(1, 100)
    vetor_random.append(a)

print(vetor_random)