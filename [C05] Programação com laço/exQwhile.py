'''
Escrever um programa que possibilite calcular a área total em metros de 
uma residência com os cômodos sala, cozinha, banheiro, dois quartos, 
área de serviço, quintal, garagem, entre outros que podem ser fornecidos 
ao programa. O programa deve solicitar a entrada do nome, da largura e 
do comprimento de um determinado cômodo. Em seguida, deve apresentar a 
área do cômodo lido e também uma mensagem solicitando ao usuário a 
confirmação de continuar calculando novos cômodos. Caso o usuário 
responda “NÃO”, o programa deve apresentar o valor total acumulado da
área residencial.
    Entendimento:
        1. Inicializar a variável [outroComodo] com valor inicial 'sim'
        2. Inicializar a variável [areaTotal] com valor inicial 0
        3. Definir a entrada de um valor cadeia, representado pela variável [nomeComodo]
        4. Definir a entrada de um valor real, representado pela variável [largura]
        5. Definir a entrada de um valor real, representado pela variável [comprimento]
        6. Realizar a operação [largura * comprimento] e imprimir e armazenar o resultado na variável [areaParcial]
        7. Acumular o valor da variável [areaParcial] na variável [areaTotal]
        8. Perguntar para usuário se deseja continuar a incluir cômodos para cálculo de área.
            1. Caso sim: repita os passos 3, 4, 5, 6 e 7.
            2. Caso não: Imprima o valor da área total
'''
outroComodo = "sim"
areaTotal = 0
while (outroComodo != "não" and outroComodo !='nao'):
    nomeComodo = input("Qual o cômodo que deseja registrar? ")
    largura = float(input(f"Qual é a largura do {nomeComodo}: "))
    comprimento = float(input(f'Qual é o comprimento do {nomeComodo}: '))
    areaParcial = largura * comprimento
    print(f'A área do {nomeComodo} é {areaParcial}.')
    areaTotal += areaParcial
    outroComodo = input("Deseja informar outro cômodo? ")
else:
    print(f'A área total da cada é {areaTotal} metros quadrados.')