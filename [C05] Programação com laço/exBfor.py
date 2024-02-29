'''
Elaborar um programa que mostre os resultados da tabuada de um número qualquer,
a qual deve ser apresentada de acordo com sua forma tradicional.
    Entendimento
        1. Inicializar a variável [i] com valor inicial de 0
        2. Definir a entrada de um valor inteiro, representado por [numero]
        3. Imprimir o resultado da multiplicação [i * numero]
        4. Incrementar [i]
        5. Repetir os passos 2 e 3 enquanto í for menor igual a 10
'''

numero = int(input("Informe um número para a tabuada: "))

for i in range(11):
    print(f"{numero} * {i:2} = { i * numero:2}")
else:
    print("Esta foi a tabuada do número {}".format(numero))