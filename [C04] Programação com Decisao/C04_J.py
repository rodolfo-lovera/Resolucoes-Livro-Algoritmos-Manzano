'''
Ler um valor numérico inteiro e apresentar uma mensagem
informando se o valor fornecido é par ou ímpar.
 Entendimento
    1. Definir a entrar de um valor inteiro, representado por [valor]
    2. Verificar se o resto do  cálculo [valor] divisão por 2 é igual a zero
	    1. Caso verdadeiro, apresentar a mensagem "PAR"
	    2. Caso falso, apresentar a mensagem "IMPAR"        
'''

valor = int(input("informe um valor inteiro qualquer: "))

if (valor % 2 == 0):
    print("Número informado é par.")
else:
    print("Número informado é impar.")