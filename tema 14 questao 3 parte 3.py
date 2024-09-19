# Lê os vetores A e B
A = [int(input("Digite o valor  do vetor A: ")) for i in range(5)]
B = [int(input("Digite o valor  do vetor B: ")) for i in range(5)]

# Troca os elementos
A, B = B, A

# Exibe os resultados
print("Vetor A:", A)
print("Vetor B:", B)
