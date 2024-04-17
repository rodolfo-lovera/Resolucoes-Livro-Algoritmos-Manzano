"""
Construir um programa que leia 15 elementos numéricos inteiros em uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmo tipo e dimensão, em que cada elemento seja o fatorial do elemento correspondente armazenado na matriz A. Apresentar os elementos da matriz B ordenados de forma crescente.
    Entendimentos:
        1. Inicializar a lista [A] vazia
        2. Efetuar a entrada de 15 elementos numéricos (verificar tipo de dado) e armazenar em [A]
        3. Inicializar a lista [B] vazia
        4. Efetuar o cálculo fatorial de cada elemento de [A] e atribuir o resultado a [B]
        5. Ordenar os elementos de [B] e apresentar ao usuário
"""
A = []

for i in range(15):

    while True:

        try:
            numero = int(input(f"Digite o {i + 1}° número inteiro: "))
            break
        except ValueError:
            print("O valor digitado não é um número inteiro.\nVamos tentar novamente.\n")
        
    A.append(numero)

print(A)

B = []

for numero in A:
    i = fatorial = 1
    
    while i <= numero:
        
        fatorial *= i 
        i += 1
    
    B.append(fatorial)

print(B, "Não ordenado")

for i in range(len(B)-1):
    for j in range(i + 1, len(B)):
        if B[i] > B[j]:

            B[i] , B[j] = B[j] , B[i]

print(B, "Ordenado")

for numero in B:
    print(numero)