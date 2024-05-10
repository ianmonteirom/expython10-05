"""
2. Preencha uma matriz 10x10 com números aleatórios e exiba a matriz. A seguir, exiba o somatório
dos elementos da diagonal secundária da matriz.
"""

from random import randint

matriz, diagSegun = [], []

for i in range(10):
    linha = []
    for j in range(10):
        n = randint(1, 99)
        linha.append(n)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
        if j - i == 1:
            diagSegun.append(matriz[i][j])
    print()


print(f'O somatório dos elementos da segunda diagonal da matriz é igual a {sum(diagSegun)}')
