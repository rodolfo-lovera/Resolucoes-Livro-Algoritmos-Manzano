''' Elaborar um programa que leia oito elementos inteiros em uma matriz A do tipo vetor.
Construir uma matriz B de mesma dimensão com os elementos da matriz A multiplicados por 3.
O elemento B[1] deve ser implicado pelo elemento A[1] * 3, o elemento B[2] implicado
pelo elemento A[2] * 3, e assim por diante, até 8. Apresentar a matriz B.
    Entendimento:
        1. Inicializar as listas [A] e [B] vazias
        2. Iniciar o contador de índice, variável [i] como 0, estendendo essa contagem até 8;
            1. Ler 8 valores, do tipo inteiro, um a um, e armazenar da lista [A];
        3. Iniciar o contador de índice, variável [i] como 0, estendendo essa contagem até 8;
            1. Multiplicar cada valor da lista [A] por 3 e atribuir a lista [B];
        4. Iniciar o contador de índice, variável [i] como 0, estendendo essa contagem até 8;
            1. Apresentar os valores armazenados em [B]
'''
A = B = []
for i in range(0,8):
    A.append(int(input(f"informe o {i+1}º valor: ")))
else:
    print("\n")

for i in range(0,8):
    B.append(A[i] * 3)

for i in range(0,8):
    print(f"O {i + 1}º valor na lista B é {B[i]}.")
else:
    print("\n")
