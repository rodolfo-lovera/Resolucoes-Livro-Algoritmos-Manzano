'''
Elaborar um programa que leia dez valores numéricos reais e
apresente no final o somatório e a média dos valores lidos.
    Entendimento:
        1. Inicializar a variável [i] com valor inicial de 1;
        2. Inicializar a variável [soma] com valor inicial de 0;
        3. Definir a entrada de um valor real, representado por [numero];
        4. Realizar a operação [soma + numero] e armazenar o resultado em [soma]
        5. incrementar a variável [i]
        6. Repetir os passos 3, 4 e 5 até i ser maior que 10
        7. Imprimir o valor da variável [soma]
'''

i = 1
soma = 0
while i <= 10:
    numero = float(input(f"informe o {i}º numero para a soma: "))
    soma += numero
    i+= 1
else:
    print(f"O resultado da soma dos dez valores é {soma}.\n")