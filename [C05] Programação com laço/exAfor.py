'''Elaborar um programa que apresente como resultado os quadrados armazenados
 na memória dos números inteiros existentes na faixa de valores de 15 a 200.
     Entendimento:
        1. Inicializar a variável [inteiro] com valor inicial 15
        2. Imprimir o resultado da operação [inteiro * inteiro]
        3. Incrementar a variável [inteiro]
        4. Repetir o passo 2 e 3 enquanto a variável [inteiro] for menor que 201
        5. Encerrar programa
'''
for inteiro in range(15,201):
    print(f"\n{inteiro}² = {inteiro * inteiro}.")
    
else:
    print("\nUm laço de repetição que mostra o quadrado dos números inteiros de 15 a 200.\n")