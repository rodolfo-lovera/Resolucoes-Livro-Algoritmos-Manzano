'''
Elaborar um programa que apresente os quadrados sem armazená-los na memória
dos valores inteiros existentes na faixa de valores de 15 a 200 com saltos 
de 3 em 3.
    Entendimento:
        1. Inicializar a variável [i] com valor inicial igual a 0
        2. Verificar se [i] é maior igual a 15 e menor igual à 200
            1. Caso sim:
                a. Imprimir a operação a operação [i * i]
                b. Incrementar a variável [i] em 3
            2. Caso não:
                a. Incrementar a variável [i] em 4
        3. Repetir o passo 2 enquanto i for menor que 201
'''
i = 0

while i < 201:
    if (i >= 15 and i <= 200):
        print(f'O quadrado de {i} é {i * i}.')
        i += 3
    else:
        i += 1
else:
    print("Acabou.")