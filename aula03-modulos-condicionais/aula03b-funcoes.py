def print_lyrics():
    print("Duality - Slipknot")
    print("I push my fingers into my eyes")
    print("It's the only thing that slowly stops the ache")
    print("But it's made of all the things i have to say")
    print("Jesus, it never ends, it works it's way inside")
    print("If the pain goes on, I'M NOT GONNA MAKE IT!")

print_lyrics()

def boas_vindas(nome):
    print(f"Olá {nome}! Seja bem vindo(a)!")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

soma(7, 5) # não exibe nada, pois apenas retorna um valor
print(soma(7, 5)) # agora exibe, pois printa o valor retornado