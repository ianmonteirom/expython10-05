"""
1. Preencha uma matriz 6x6 com o elemento 1 em todas as posições em que o índice de linha tem valor
igual ao índice da coluna. Preencha os demais elementos com zero e exiba a matriz.
"""

matriz = []

for i in range(6):
    linha = []
    for j in range(6):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()
