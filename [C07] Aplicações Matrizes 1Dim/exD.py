

A = []

for i in range(12):
    
    while True:
    
        try:
            valor = float(input(f"Digite o {i + 1}° valor real para a lista A: "))
            break 
        except ValueError:
            print("Valor informado não é real. Vamos tentar novamente.\n")
    
    A.append(valor)

print(A)

for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            A[i] , A[j] = A[j] , A[i]

print(A, "Lista A ordenada.")

B = []

for i in range(12):

    while True:

        try:
            valor = float(input(f"Digite o {i + 1}° valor real para a lista B:"))
            break
        except ValueError:
            print("Valor informado não é real. Vamos tentar novamente.\n")
    
    B.append(valor)

print(B)

for i in range(len(B) - 1):
    for j in range(i + 1, len(B)):
        if B[i] > B[j]:
            B[i] , B[j] = B[j] , B[i]

print(B, "Lista B ordenada.")

C = []

for i in range(12):
    C.append(A[i] + B[i])

for i in range(len(C) - 1):
    for j in range(i + 1, len(C)):
        if C[i] < C[j]:
            C[i] , C[j] = C[j] , C[i]

for i in range(12):
    print(f"Este é o {i + 1}° valor da lista C: {C[i]}.")