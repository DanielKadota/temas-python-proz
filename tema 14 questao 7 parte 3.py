# Lê a matriz
matriz = [[int(input("Digite o valor para a posição : ")) for j in range(4)] for i in range(7)]

# Encontra o menor valor e sua posição
menor = min(min(linha) for linha in matriz)
posicao = [(i, linha.index(menor)) for i, linha in enumerate(matriz) if menor in linha][0]

# Exibe os resultados
print("Menor valor:", menor)
print("Posição do menor valor:", posicao)
