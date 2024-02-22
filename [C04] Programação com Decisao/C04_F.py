'''
 Ler três valores inteiros representados pelas variáveis A, B e C e apresentar os valores lidos
 dispostos em ordem crescente. Dica: utilizar tomada de decisão sequencial e as ideias trabalhadas
 nos exercícios “g” (propriedade distributiva) e “f” (troca de valores) do Capítulo 3.
  Entendimento:
    1. Definir a entrada de 3 valores inteiros, representados por [A, B e C];
    2. Verificar se A é maior que B:
      1. Caso seja verdadeiro, verificar se B é maior que C
        a. caso verdadeiro, não fazer nada [A B C]
        b. caso falso, verificar se C é maior que A
	  		i. caso verdadeiro trocar os valores [C A B]
	  		ii. caso falso, trocar os valores [A C B]
	  2. Caso seja falso, verificar se A é maior de C
		a. caso verdadeiro, trocar os valores de [B A C]
		b. caso falso, verificar se B é maior que C
			i. caso verdadeiro, trocar os valores [ B C A]
			ii. caso falso, trocar os valores [C B A]
    3. Apresentar os valores de [A, B e C]
'''

A = int(input("informe um valor inteiro qualquer: "))
B = int(input("informe outro valor inteiro qualquer: "))
C = int(input("informe mais um outro valor inteiro qualquer: "))

if (A > B):
    if (B > C):
        print("\n") # A , B , C
    else:
        if (C > A): # C , A , B
            x = B
            B = A
            A = C
            C = x
        else:  # A , C , B
            x = B
            B = C
            C = x
else:
    if (A > C): # B , A , C
        x = B
        B = A
        A = x
    else:
        if (B > C): # B , C , A
            x = A
            A = B
            B = C
            C = x
        else: # C , B , A
            x = A
            A = C
            C = x 
print("A ordem de valores é {}, {} e {}".format(A, B, C))