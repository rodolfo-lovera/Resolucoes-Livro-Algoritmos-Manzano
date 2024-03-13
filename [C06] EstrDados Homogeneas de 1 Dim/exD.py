'''Elaborar um programa que leia 15 elementos inteiros de uma matriz A do tipo vetor.
Construir uma matriz B de mesmo tipo, observando a seguinte lei de formação:
“todo elemento da matriz B deve ser o quadrado do elemento da matriz A correspondente”.
Apresentar os elementos das matrizes A e B.
    Entendimento:
    1. Inicializar as listas A e B vazias;
    2. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 15;
        1. Ler 15 valores do tipo inteiro, um a um e armazenar em [A]
    3. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 15;
        1. Multiplicar cada valor armazenado em [A] por ele mesmo e atribuir em [B]
    4. Iniciar o contador de índice, variável [i] como 0 estendendo essa contagem até 15;
        1. Apresentar os valores armazenados em [B]
'''

A = B = []

for i in range(0,15):
    if i == 0:
        A.append(int(input("Informe o primeiro valor inteiro: ")))
    elif i == 14:
        A.append(int(input("Informe o ultimo valor inteiro: ")))
    else:
        A.append(int(input("Informe mais um valor inteiro: ")))

for i in range(0,15):
    B.append(pow(A[i],2))

for i in range(0,15):
    print(f"{A[i]}² = {B[i]}. ")