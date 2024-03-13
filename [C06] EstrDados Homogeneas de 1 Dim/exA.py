'''
Elaborar um programa que efetue a leitura de dez nomes de pessoas em uma matriz A
do tipo vetor e apresentá-los em seguida.
    Entendimento:
        1. iniciar o contador de índice, variável [i] como 1, estendendo essa contagem até 10;
        2. Ler dez nomes, um a um, armazenando em uma lista [listaNome];
        3. Apresentar o conteúdo da lista [listaNome];
'''
listaNome = []
for i in range(0,10):
    listaNome.append(input(f"Insira o {i + 1}º nome: "))
else:
    print("\n\n")

for i in range(0,10):
    print(f"O {i + 1}ª nome informado foi {listaNome[i]}.")
