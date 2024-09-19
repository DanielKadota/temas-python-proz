# Definindo os pares de números
pares = [(10, 2), (6, 2), (15, 3)]
A = 0
C = 0

# Processando cada par
for x, y in pares:
    A += x
    C += x // y

# Exibe os resultados finais
print("Valor final de A:", A)
print("Valor final de C:", C)
