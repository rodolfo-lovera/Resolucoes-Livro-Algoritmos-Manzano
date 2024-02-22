'''
 Efetuar a leitura de dois valores numéricos inteiros representados pelas
  variáveis A e B e apresentar o resultado da diferença do maior valor
  pelo menor valor.
   Entendimento:
    1. Definir a entrada de dois valores, representados por [a] e [b];
    2. Efetuar a subtração dos valores [a] e [b] e atribuir o resultado à [resultado]
    3. Verificar se o valor de [resultado] e inferior a zero
        1. caso seja menor, multiplicar o valor por -1
    4. Apresentar o resultado da variável [resultado]
'''

a = int(input("Forneça um valor inteiro qualquer: "))
b = int(input("Forneça outro valor inteiro: "))

resultado = a - b

if (resultado < 0 ):
    resultado *= -1

print(f"\nO resultado da diferença do maior pelo menor é {resultado}.\n")