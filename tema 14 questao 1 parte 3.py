# Lê os valores do vetor
valores = [int(input(f"Digite o valor {i + 1}: ")) for i in range(10)]

# Calcula a diferença
maior = max(valores)
menor = min(valores)
diferenca = maior - menor

# Exibe o resultado
print("Diferença entre o maior e o menor elemento:", diferenca)
