'''
Construir um programa que apresente todos os valores numéricos divisíveis por 4 e menores que 200.
Sugestão: a variável que controla o contador do laço deve ser iniciada com valor 1.
    Entendimento:
        1. Inicializar a variável [i] com valor inicial de 1;
        2. Se o resto da operação [i / 4] for igual a zero, imprima o resultado
        3. incremente a variável [i]
        4. Repetir os passos 2 e 3 enquanto i for menor que 200
        5. Encerrar programa;
'''

for i in range(1,200):
    if (i % 4 == 0):
        print(i , end=' ')    
else:  
    print(". Estes são todos os números divisíveis por 4 e menores que 200.\n Acabou o programa.")