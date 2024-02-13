'''
 Construir um programa que leia três valores numéricos inteiros (representados pelas variáveis A, B e C)
 e apresentar como resultado final, armazenado em memória, o valor do quadrado da soma dos três valores lidos.
 Entendimento:
  1. Ler três valores desconhecidos, representados pelas variáveis [a, b e c];
  2. Efetuar o cálculo [quadradoDaSoma = (a + b + c)*(a + b + c)]
  3. Efetuar o cálculo [somaDosQuadrados = a*a + b* b + c *c]
  4. Apresentar os resultados das variáveis [quadradoDaSoma; somaDosQuadrados]
'''

a = int(input('informe um valor inteiros, que será armazenado em [a]: '))
b = int(input("Informe um valor inteiro, que será armazenado em [b]: "))
c = int(input('Informe um valor inteiro, que será armazenado em [c]'))

quadradoDaSoma = (a + b + c)*(a + b + c)
somaDosQuadrados = a*a + b* b + c *c

print('O quadrado da soma dos valores é ', quadradoDaSoma, f"e a soma dos quadrados é {somaDosQuadrados}.")