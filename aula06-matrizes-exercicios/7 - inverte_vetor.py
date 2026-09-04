n = int(input("Digite a quantidade de posições que deseja que o vetor tenha: "))
while n < 0:
    print("Número inválido. Digite apenas valores positivos")
    n = int(input("Digite a quantidade de posições que deseja que o vetor tenha: "))

vetor = []
for num in range(1, n+1):
    vetor.append(num)

print()
print(f"Este é o vetor normal: {vetor}")

for i in range(len(vetor)//2):
    vetor[i], vetor[-1-i] = vetor[-1-i], vetor[i]

print()
print(f"Este é o vetor invertido: {vetor}")