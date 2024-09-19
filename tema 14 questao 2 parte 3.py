# Lê os valores do vetor
valores = [int(input("Digite o valor {i + 1}: ")) for i in range(10)]

# Soma os elementos de índice par
soma = sum(valores[i] for i in range(0, 10, 2))

# Exibe o resultado
print("Soma dos elementos de índice par:", soma)
