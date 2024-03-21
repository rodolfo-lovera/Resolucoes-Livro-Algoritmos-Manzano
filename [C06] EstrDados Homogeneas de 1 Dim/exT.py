''' Escrever um programa que leia duas matrizes A e B de uma dimensão com dez elementos. A matriz A deve aceitar apenas a entrada de valores divisíveis por 2 e 3, enquanto a matriz B deve aceitar apenas a entrada de valores múltiplos de 5. A entrada das matrizes deve ser validada pelo programa, e não pelo usuário. Construir uma matriz C que seja o resultado da junção das matrizes A e B, de modo que contenha 20 elementos. Apresentar os elementos da matriz C.
    Entendimento:    
    1. Inicializar as lista [A] e [B] vazias
    2. Ler um valor inteiro informado pelo usuário
    3. Verificar se valor informado é divisível por 6
        1. Sim: armazenar na lista [A]
    4. Repetir os passos 2 e 3 até o tamanho da lista [A] ser igual a 10
    5. Ler uma valor inteiro informado pelo usuário
    6. Verificar se valor informado é divisível por 5
        1. Sim: armazenar na lista [B]
    7. Repetir os passos 5 e 6 até o tamanho da lista [B] ser igual a 10
    8. inicializar a lista [C] 
    9. Atribuir os elementos de A e B para a lista C
    10. Apresentar os elementos da lista [C]
'''
A = []

while (len(A) <= 4):
    valor = int(input("Informe um valor númerico inteiro (A): "))

    if ((valor % 6) == 0):
        A.append(valor)

    else:
        print("Valor não é divisível por 6.")
else:
    print("Rotina de entrada para A terminou.\n")
    

B = []

while (len(B) <= 4):
    valor = int(input("Informe um valor númerico inteiro (B): "))

    if ((valor % 5) == 0):
        B.append(valor)
        
    else:
        print("Valor não é múltiplo de 5.")
else:
    print("Rotina de entrada para B terminou.\n")
    

C = []

for i in A:
    C.append(i)

for i in B:
    C.append(i)

for i in C:
    print(f"valor armazenado em C: {i}")