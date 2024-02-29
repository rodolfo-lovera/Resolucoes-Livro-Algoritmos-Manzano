'''
Construir um programa que apresente a soma dos cem primeiros números naturais (1 + 2 + 3 +...+ 98 + 99 + 100).
    Entendimento:
        1. Inicializar as variáveis [i] e [somatorio] com valor inicial de 1 e 0, respectivamente;
        2. Realizar a operação [i + somatorio] e armazenar o resultado em [somatorio]
        3. Imprimir o resultado de [somatorio]
        4. Incrementar a variável [i]
        5. Repetir os passos 2, 3 e 4
        6. Imprimir o valor de [somatório]

'''
i = 1
somatorio = 0

while (i < 101):
    somatorio = somatorio + i
    print(f"{i}ª soma: {somatorio}.")
    i += 1
else:
    print("O resultado da soma dos 100 primeiros números é {}.".format(somatorio))
