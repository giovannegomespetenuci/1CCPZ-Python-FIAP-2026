lista_frutas = ["Banana", "Maçã", "Morango"]

print(lista_frutas)

lista_frutas.append("Uva") # adiciona um elemento no final do array
print(lista_frutas[-1]) # tamanho do array menos 1 (4 - 1 = 3)

tamanho = len(lista_frutas) # tamanho total do array
print(tamanho)

for i in range(tamanho):
    print(lista_frutas[i]) # forma de listar todos os elementos do array um por vez

print()

for fruta in lista_frutas:
    print(fruta) # outra forma de listar os elementos, associando-os à "fruta"

print()

msg = "oi jovas"
print(msg[1]) # strings são arrays de caracteres, logo podem ser manipulados como tal
print()
for i in range(len(msg)):
    print(msg[i])