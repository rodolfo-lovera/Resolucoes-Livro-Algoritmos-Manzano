'''
 Construir um programa que calcule, armazene e apresente em metros por segundo o valor da velocidade
 de um projétil que percorre uma distância em quilômetros a um espaço de tempo em minutos.
 Utilize a fórmula VELOCIDADE ← (DISTÂNCIA * 1000) / (TEMPO * 60).
 Entendimento:
  1. Ler dois valores desconhecidos, representados pelas variáveis [distancia(float); tempo(float)];
  2. Efetuar o cálculo [velocidade ← (distância * 1000) / (tempo * 60)];
  3. Apresentar o resultado da variável [velocidade].
'''

distancia = float(input('Qual é a distância (km) percorrida pelo projétil? '))
tempo = float(int(input("Qual foi o tempo (min) gasto para percorrer a distância? ")))

velocidade = (distancia * 1000) / (tempo * 60)

print("A velocidade média do projétil foi de {} m/s.".format(velocidade))