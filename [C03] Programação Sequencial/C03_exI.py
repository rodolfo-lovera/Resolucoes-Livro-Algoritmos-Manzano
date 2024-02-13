'''
 Efetuar a leitura de um valor numérico inteiro e apresentar o resultado do valor lido elevado ao quadrado,
 sem efetuar o armazenamento do resultado em memória.
  Entendimento
   1. ler o valor desconhecido, representados pela variável [valor];
   2. Apresentar o resultado do cálculo [valor * valor]
  
'''

valor = int(input("informe um valor qualquer: "))
print("O quadrado de {} é {}".format(valor, valor*valor))