"""
3. Preencha uma matriz 6x6 com números aleatórios e multiplique cada elemento da matriz pelo maior
elemento de sua linha. Escrever a matriz original e a modificada.
"""

from random import randint

matriz, maiores = [], []

for i in range(6):
    linha = []
    for j in range(6):
        n = randint(1, 50)
        linha.append(n)
    matriz.append(linha)

for i in range(len(matriz)):
    maiorLinha = 0
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
        if matriz[i][j] > maiorLinha:
            maiorLinha = matriz[i][j]
    maiores.append(maiorLinha)
    print()

print('--' * 32)
print(f'Maiores valores de cada linha: {maiores}')

novaMatriz = []

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] *= maiores[i]
        print(matriz[i][j], end='\t')
    print()

# print(maiores)
