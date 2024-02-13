"""
 Ler uma temperatura em graus Celsius e apresentá-la convertida em graus
 Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32, sendo F a
 temperatura em Fahrenheit e C a temperatura em Celsius.
  Entendimento
    1. Ler um valores desconhecido, representado pela variável [C] (float);
    2. Efetuar o cálculo de conversão [F = C * (9 / 5) + 32]
    3. Apresentar o valor na variável [F]
"""
C = float(input("Digite um valor de temperatura para converter "))
F = C * (9 / 5) + 32
print(f"\nO valor da temperatura em {C} °C é  e em Fahrenheit é {F} °F.\n")