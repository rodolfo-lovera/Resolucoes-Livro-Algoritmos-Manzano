''' Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas
 pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e apresentar
 a mensagem “Aprovado” se a média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem
 “Reprovado”. Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.
   Entendimento:
    1. Definir a entrada de 4 valores, representados por [N1; N2; N3; N4]
    2. Efetuar o cálculo da média dos valores [N1; N2; N3; N4] e atribuir o resultado à [MD]
    3. Verificar se o valor de [MD] é maior ou igual à 6:
	  1. Caso seja maior, apresentar a mensagem "Aprovado com média" e apresentar o valor da variável [MD]
	  2. Caso seja menor, apresentar a mensagem "Reprovado com média" e apresentar o valor da variável [MD]
'''

N1 = float(input("informe a nota do primeiro bimestre: "))
N2 = float(input("informe a nota do segundo bimestre: "))
N3 = float(input("informe a nota do terceiro bimestre: "))
N4 = float(input("informe a nota do quarto bimestre: "))

MD = (N1 + N2 + N3 + N4)/4

if (MD >= 6):
    print("\nAprovado com média {}.\n".format(MD))
else:
    print("\nReprovado com média {}.\n".format(MD))