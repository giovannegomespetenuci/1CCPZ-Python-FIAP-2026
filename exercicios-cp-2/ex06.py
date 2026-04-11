import sys

print("CALCULADORA")
num1 = float(input("Insira um número: "))
op = input("Insira a operação (+, -, *, /): ")
if op not in ["+", "-", "*", "/"]:
    print("Insira uma operação válida!")
    sys.exit() # fecha o programa
num2 = float(input("Insira outro número: "))

match op:
    case "+":
        resul = num1 + num2
        print(f"O resultado de {num1} {op} {num2} é {resul}")
    case "-":
        resul = num1 - num2
        print(f"O resultado de {num1} {op} {num2} é {resul}")
    case "*":
        resul = num1 * num2
        print(f"O resultado de {num1} {op} {num2} é {resul}")
    case "/":
        resul = num1 / num2
        print(f"O resultado de {num1} {op} {num2} é {resul}")
    case _:
        print("Erro")