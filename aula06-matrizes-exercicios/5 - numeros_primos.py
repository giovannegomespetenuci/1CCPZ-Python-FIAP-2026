for n in range(2, 2001):
    divisores = []
    for i in range(1, n+1):
        if n % i == 0:
            divisores.append(i)

    if len(divisores) <= 2:
        print(f"O número {n} é primo")