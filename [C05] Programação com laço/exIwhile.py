'''
Escrever um programa que apresente os valores da sequência numérica de Fibonacci até o décimo quinto termo.
A sequência de Fibonacci é formada pelos valores numéricos 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ... etc.,
obtendo-se o próximo termo a partir da soma do termo atual com o anterior sucessivamente até o infinito se a sequência não
for interrompida, sendo determinada a partir da fórmula Fn = Fn-1 + Fn-2. Utilize para este exercício as variáveis ATUAL, ANTERIOR e PRÓXIMO.
    Entendimento:
        1. Inicializar a variável [i] com valor inicial de 1
        2. Inicializar as variáveis [atual; anterior, proximo] com valor inicial 0;
        3. Verificar se atual é igual a zero:
            1. Caso seja verdadeiro, imprimir valor e incrementar 1;
            2. Caso seja falso, realizar a operação [próximo = atual + anterior]
            3. Imprimir [proximo]
            4. Realizar as atribuições: [anterior = atual] e [atual = proximo]
        4. Incrementar [i] em 1
        5. Repetir os passos 3 e 4 até i ser maior que 15;
        6. Encerrar programa
'''
i = 0
atual = 0
anterior = 0
proximo = 0

while i < 15:
    if atual == 0:
        print(f"{atual},", end='')
        atual += 1
    else:
        proximo = atual + anterior
        print(proximo,',',end='')
        anterior = atual
        atual = proximo
    i += 1
else:
    print(".\n")


'''esta foi a primeira solução mas o resultado estava dando errado (0,1 ,2 ,3 ,5 ,8 ,13 ,21 ,34 ,55 ,89 ,144 ,233 ,377 ,610 ,.)

refiz o código e ficou desse jeito:
    i = 0
    while i < 15:
        print(atual)

        if i == 1:
            proximo = 1
        else:
            proximo = atual + anterior

        anterior = atual
        atual = proximo
        i += 1

'''