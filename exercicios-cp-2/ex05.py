num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

if num1 < num2:
    num1, num2 = num2, num1

if num1 % num2 == 0:
    print(f"{num1} e {num2} são múltiplos")
else:
    print(f"{num1} e {num2} não são múltiplos")