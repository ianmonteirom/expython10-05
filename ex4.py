"""
4. Preencha uma matriz 4x4 com números informados pelo usuário e exiba a matriz. Na sequência, gere
a transposta da matriz e exiba-a (matriz transposta é a matriz que se obtém da troca de linhas por
colunas da matriz)
"""

matriz, linhas, colunas = [], [], []

for i in range(4):
    linha = []
    for j in range(4):
        n = int(input(f'Número da posição [{i}, {j}]: '))
        linha.append(n)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()
