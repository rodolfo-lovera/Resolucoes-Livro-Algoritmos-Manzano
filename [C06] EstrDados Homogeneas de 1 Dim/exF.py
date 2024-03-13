'''Construir um programa que leia duas matrizes A e B do tipo vetor com 15 elementos quaisquer inteiros.
Construir uma matriz C, sendo esta o resultado da junção das matrizes A e B. Desta forma, a matriz C
deve ter o dobro de elementos em relação às matrizes A e B, ou seja, a matriz C deve possuir 30 elementos.
Apresentar a matriz C.
    Entendimento:
        1. Inicializar as listas [A], [B] e [C] vazias;
        2. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 15;
            1. Ler 15 valores do tipo inteiro, um a um e armazenar em [A]
        3. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 15;
            1. Ler 15 valores do tipo inteiro, um a um e armazenar em [B]
        4. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 30;
            1. Verificar se a quantidade de elementos em [C] é menor que 15:
                a. Verdade: Armazenar os valores de [A] em [C];
                b. Falso: Armazenar os valores de [B] em [C];
        5. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 30;
            1. Apresentar os valores de C]
'''

A = B = C = []

for i in range(0,15):
    A.append(int(input(f"Informe o {i + 1}º valor para a lista A: ")))

for i in range(0,15):
    B.append(int(input(f"Informe o {i + 1}º valor para a lista B: ")))

for i in range(0,30):
    if (len(C) < 15):
        C.append(A[i])
    else:
        C.append(B[i])

for i in range(0,30):
    print(f"{i + 1}º da lista C = {C[i]}.")