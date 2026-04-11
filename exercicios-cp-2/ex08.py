salario = float(input("Insira o salário: "))
if salario <= 280:
    aumento = "20%"
    valor_aumento = salario * 0.2
    novo_salario = salario * 1.2
    print(f"O salário antigo era de {salario}")
    print(f"O percentual de aumento é de {aumento}")
    print(f"O valor acrescentado foi de {valor_aumento}")
    print(f"O novo salário é de {novo_salario}")
elif salario <= 700:
    aumento = "15%"
    valor_aumento = salario * 0.15
    novo_salario = salario * 1.15
    print(f"O salário antigo era de {salario}")
    print(f"O percentual de aumento é de {aumento}")
    print(f"O valor acrescentado foi de {valor_aumento}")
    print(f"O novo salário é de {novo_salario}")
elif salario <= 1500:
    aumento = "10%"
    valor_aumento = salario * 0.1
    novo_salario = salario * 1.1
    print(f"O salário antigo era de {salario}")
    print(f"O percentual de aumento é de {aumento}")
    print(f"O valor acrescentado foi de {valor_aumento}")
    print(f"O novo salário é de {novo_salario}")
elif salario > 1500:
    aumento = "5%"
    valor_aumento = salario * 0.05
    novo_salario = salario * 1.05
    print(f"O salário antigo era de {salario}")
    print(f"O percentual de aumento é de {aumento}")
    print(f"O valor acrescentado foi de {valor_aumento}")
    print(f"O novo salário é de {novo_salario}")