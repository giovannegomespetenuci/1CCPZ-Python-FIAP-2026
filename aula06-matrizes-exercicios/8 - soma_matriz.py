matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz2 = [
    [4, 7, 2],
    [7, -3, -10],
    [-4, 61, 58]
]
matriz3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

linhas = len(matriz1)
colunas = len(matriz1[0])

for i in range(linhas):
    for j in range(colunas):
        matriz3[i][j] = matriz1[i][j] + matriz2[i][j]

for linha in range(len(matriz3)):
    print(matriz3[linha])