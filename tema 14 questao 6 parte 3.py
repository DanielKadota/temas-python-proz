# Inicializa a matriz
matriz = [[int(input("Digite o valor para a posição : ")) for j in range(6)] for i in range(5)]
pares = [num for linha in matriz for num in linha if num % 2 == 0]

# Calcula a média
media = sum(pares) / len(pares) if pares else 0

# Exibe a matriz e a média
print("Matriz:")
for linha in matriz:
    print(linha)
print("Média dos valores pares:", media)
