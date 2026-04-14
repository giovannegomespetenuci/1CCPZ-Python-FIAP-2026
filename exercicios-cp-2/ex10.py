a = int(input("Insira o primeiro lado do triângulo: "))
b = int(input("Insira o segundo lado do triângulo: "))
c = int(input("Insira o terceiro lado do triângulo: "))
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

mensagem = ""
if a >= (b+c):
    mensagem = "Não forma um triângulo"
elif a**2 == (b**2 + c**2):
    mensagem = "Triângulo retângulo"
elif a**2 > (b**2 + c**2):
    mensagem = "Triângulo obtusângulo"
elif a**2 < (b**2 + c**2):
    mensagem = "Triângulo acutângulo"
elif a == b == c:
    mensagem = "Triângulo equilátero"
elif a == b or b == c or a == c:
    mensagem = "Triângulo isósceles"
print(mensagem)