''' Elaborar um programa que leia uma matriz A do tipo vetor com 20 elementos inteiros. Construir uma matriz B dos mesmos tipo e dimensão da matriz A, sendo cada elemento da matriz B o somatório de 1 até o valor do elemento correspondente armazenado na matriz A. Se o valor do elemento da matriz A[1] for 5, o elemento correspondente da matriz B[1] deve ser 15, pois o somatório do elemento da matriz A é 1 + 2 + 3 + 4 + 5. Apresentar os elementos da matriz B.
    Entendimento:
        1. Inicializar as lista [A] e [B] vazias
        2. Iniciar o contador de índice [i] como 0 estendendo contagem até 20;
            1. Ler 20 valores inteiro e armazenar em [A]
        3. Iniciar o contador de índice, [numeroA] como elementos da lista [A]
            1. Inicializar a variável [acumulador] com valor 0
            2. Enquanto [acumulador] é menor que [numeroA]
                a. Incremente em 1
            3. Transfira acumulador para a lista B           
                
        4. Apresentar os valores da lista [B]
'''

A = B = []

print("Forneça 20 valores inteiros positivos.")
for i in range(0, 20):
    A.append(int(input(f"Informe o {i + 1}º valor: ")))

print(f"Esta é a lista A: {A}")
print(f"Esta é a lista B: {B}\n")

for i in range(0,20):
    print(f"Este é o item {i + 1} da lista A: {A[i]}")
    acumulador = 0
    contador = 0
    
    for contador in range(0, A[i]+1):
        acumulador += contador
        print(f"valor acumulado no ciclo {contador}: {acumulador}")
    
    B.append(acumulador)
    print(f"Este é o item {i + 1} da lista B: {B[i]}\n")

for i in range(0, 20):
    print(f'{i + 1}ª valor: {B[i]}') 