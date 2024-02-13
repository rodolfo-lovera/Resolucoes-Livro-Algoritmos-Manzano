'''
 e. Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso,
 utilizando a fórmula PRESTAÇÃO ← VALOR + (VALOR * (TAXA / 100) * TEMPO).
  Entendimento:
  1. Ler os valores desconhecidos, representados pelas variáveis: [valor; taxa; tempo];
  2. Efetuar o cálculo [prestacao = valor + (valor * (taxa / 100) * tempo)]
  3. Apresentar o valor da variável [prestacao]
'''

valor = float(input("Informe o valor da prestação em atraso: "))
tempo = int(input("Informe o tempo de atraso, em meses: "))
taxa = float(input("Informe qual é a taxa de juros, em %: "))

prestacao = valor + (valor * (taxa / 100) * tempo)

print(f"A prestação a ser paga, devido o atraso de {tempo} meses com uma taxa de {taxa}, é de R$ {prestacao}.")
print("A prestação a ser paga, devido o atraso de {} meses com uma taxa de {}, é de R$ {}.".format(tempo,taxa,prestacao))


