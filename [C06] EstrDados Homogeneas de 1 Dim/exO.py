'''Escrever um programa que leia 25 elementos (valores reais) para temperaturas em graus Celsius e armazene esses valores em uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmos tipo e dimensão, em que cada elemento da matriz B deve ser a conversão da temperatura em graus Fahrenheit do elemento correspondente da matriz A. Apresentar os elementos das matrizes A e B.'''

import numpy as np

n_elementos = 5
A = np.zeros(n_elementos)
B = np.zeros(n_elementos)

for i in range(n_elementos):
    temperatura_celsius = float(input(f"Informe a {i + 1}ª temperatura (°C): "))
    A[i] = temperatura_celsius

for i in range(n_elementos):
    temperatura_fahrenheit = (A[i] * 9/5) + 32
    B[i] = temperatura_fahrenheit

print("\nMatriz A (temperatura em °C):")
for i in range(n_elementos):
    print(f"{i + 1}: {A[i]:.2f}")

print("\n\nMatriz B (temperatura em °F): ")
for i in range(n_elementos):
    print(f'{i + 1}: {B[i]:.2f}')