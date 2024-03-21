'''Elaborar um programa que leia 20 elementos (valores reais) para temperaturas em graus Celsius e armazene esses valores em uma matriz A de uma dimensão. O programa ao final deve apresentar a menor, a maior e a média das temperaturas lidas.
    Entendimento:
        1. Inicializar a lista [A] vazia
        2. Inicializar as variáveis [maior], [menor] e [media] com valores iniciais 0
        3. Iniciar o contador de índice [i] como 0 estendendo contagem até 20;
            1. Ler 20 valores reais e armazenar em [A]
        4. Iniciar contador [numeros] percorrendo todos os elementos da lista [A]
            1. Acumular o valor de [numeros] na variável [média]
            2. Verificar se valor de [numeros] é menor que [menor]
                a. Verdade: atribuir valor a variável [menor]
            3. Verificar se valor de [numeros] é maior que [maior]
                a. Verdade: atribuir valor a variável [mãior]
        5. Realizar a operação [media] / [tamanho [A]]
        6. Apresentar os valores das variáveis [maior], [menor] e [media]
'''

A = []
menor = maior = media = 0


for i in range(0, 20):
    A.append(float(input(f"Informe a {i + 1}º temperatura em °C: ")))

for numeros in A:    
    media += numeros

    if menor == 0:
        menor = numeros
    
    if numeros < menor:
        menor = numeros
    
    if numeros > maior:
        maior = numeros

media = media / (len(A))

print(f"A menor temperatura informador foi de {menor}° C, a maior foi de {maior}° e a média das temperaturas informadas foi de {media}°C.")