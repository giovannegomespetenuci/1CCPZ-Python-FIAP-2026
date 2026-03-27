nome = input("Insira o nome do colaborador: ")
valor_hora = float(input("Insira o valor da hora trabalhada: "))
quant_hora = float(input("Insira a quantidade de horas trabalhadas: "))
bonus = float(input("Insira o valor do bônus: "))
desconto = float(input("Insira o valor descontado do salário: "))

bruto = valor_hora * quant_hora + bonus
liquido = bruto - desconto

print(f"Nome do colaborador(a): {nome}")
print(f"Salário bruto: R${bruto:.2f}")
print(f"Salário líquido: R${liquido:.2f}")