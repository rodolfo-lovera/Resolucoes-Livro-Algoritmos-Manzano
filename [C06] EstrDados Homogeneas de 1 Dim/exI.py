'''Escrever um programa que leia três matrizes (A, B e C) de uma dimensão do tipo vetor com cinco elementos cada que sejam do tipo real. Construir uma matriz D, sendo esta o resultado da junção das três matrizes (A, B e C). Desta forma, a matriz D deve ter o triplo de elementos das matrizes A, B e C, ou seja, 15 elementos. Apresentar os elementos da matriz D.
    Entendimento:
        1. Inicializar as listas [A], [B] e [C] vazias
        2. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 5;
            1. Ler 5 valores do tipo inteiro, um a um e armazenar em [A]
        3. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 5;
            1. Ler 5 valores do tipo inteiro, um a um e armazenar em [B]
        4. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 5;
            1. Ler 5 valores do tipo inteiro, um a um e armazenar em [C]
        5. Inicializar a lista [D] vazia
        6. Iniciar o contador de índice, variável [item] como elementos da lista [A];
            1. Transferir cada elemento da lista A para a lista D
        7. Iniciar o contador de índice, variável [item] como elementos da lista [B];
            1. Transferir cada elemento da lista B para a lista D
        8. Iniciar o contador de índice, variável [item] como elementos da lista [C];
            1. Transferir cada elemento da lista C para a lista D
        9. Iniciar o contador de índice, variável [item] como elementos da lista [D];
            1. Apresentar a variável Item
'''

A = B = C = []
for i in range(0, 5):
    A.append(int(input(f"Informe o {i + 1}º valor: ")))

for i in range(0, 5):
    B.append(int(input(f"Informe o {i + 1}º valor: ")))

for i in range(0, 5):
    C.append(int(input(f"Informe o {i + 1}º valor: ")))

D = []

for item in A:
    D.append(item)

for item in B:
    D.append(item)

for item in C:
    D.append(item)

for item in D:
    print(item)