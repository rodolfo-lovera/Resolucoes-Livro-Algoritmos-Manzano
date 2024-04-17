"""Elaborar um programa que leia 12 elementos numéricos inteiros em uma matriz do tipo vetor. Coloque-os em ordem decrescente e apresente os elementos ordenados.
    Entendimento:
        1. Definir uma variável de controle para execução dos laços
        2. Inicializar a lista [numerosInteiros] vazia
        3. Efetuar a entrada de 12 valores numéricos inteiros (verificação de tipos)
        4. Colocar em ordem descendentes
        5. Apresentar os 12 números armazenados na lista [numerosInteiros]
"""

numerosInteiros = []

for i in range (0,12):

    while True:

        try:
            numero = int(input(f"Digite o {i + 1}º número inteiro: "))
            break
        except ValueError:
            print("O valor digitado não é um número inteiro. Tente novamente.")

    numerosInteiros.append(numero)

print(numerosInteiros)

for i in range(0, 11):

    x = ''

    for j in range(i + 1, 12):
        if numerosInteiros[i] < numerosInteiros[j]:
            x = numerosInteiros[i]
            numerosInteiros[i] = numerosInteiros[j]
            numerosInteiros[j] = x

print(numerosInteiros)

for i in range(12):
    print(f"O {i + 1}º valor é {numerosInteiros[i]}.")