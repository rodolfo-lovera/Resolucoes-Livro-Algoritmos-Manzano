"""
Elaborar um programa que leia oito elementos numéricos inteiros em uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmos tipo e dimensão com os elementos da matriz A multiplicados por 5. Montar uma rotina de pesquisa binária para pesquisar os elementos armazenados na matriz B.
    Entedimento:
        1. Inicializar a lista [A] vazia
        2. Efetuar a entrada de 8 valores numéricos inteiros e atribuir a lista [A]
        3. Inicializar a lista [B] vazia
        4. Multiplicar cada valor armazenado em [A] por 5 e atribuir a lista [B]
        5. Ordenar os elementos da lista [B]
        6. Realizar a pesquisa binário na lista [B] de um elementos informado pelo usuário
        7. Repetir a busca enquanto o usuário desejar
"""

A = [] 

for i in range(8):
    valor = int(input(f"Digite o {i + 1}° elemento da matrix A: "))
    A.append(valor)

print(A)

B = []

for elemento in A:
    B.append(elemento * 5)

for i in range(len(B)):
    for j in range(i + 1, len(B)):
        if B[i] > B[j]:
            B[i], B[j] = B[j], B[i]

print(B)

continua = ''

while True:

    valor_pesquisado = int(input("Digite o valor que deseja pesquisar: "))

    esquerda = 0
    direita = len(B) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if B[meio] == valor_pesquisado:
            print(f"O valor {valor_pesquisado}  foi encontrado na matriz B.")
            break

        if B[meio] < valor_pesquisado:
            esquerda = meio + 1
        else:
            direita = meio - 1

    if esquerda > direita:
        print(f"O valor {valor_pesquisado} não foi encontrado na matriz B.")
    
    continua = input('Deseja procurar outro valor (sim ou não): ')

    if (continua == "não") or (continua == "Não") or (continua == "NÃO"):
        break
