'''
Ler um número inteiro qualquer e multiplicá-lo por dois.
Apresentar o resultado da multiplicação somente se o resultado for maior que 30.
 Entendimento:
    1. Definir a entrada de um valor inteiro, representado por N
    2. Verificar se o resultado da multiplicação de N * 2 é maior que 30:
      	1. Caso verdadeiro, apresentar o resultado.
'''

N = int(input("Informe um valor inteiro qualquer: "))

if (N * 2 > 30):
    print(N * 2)