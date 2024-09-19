# Lê o vetor
N = [int(input("Digite o valor : ")) for i in range(20)]

# Encontra o menor elemento e sua posição
menor = min(N)
posicao = N.index(menor)

# Exibe os resultados
print("Menor elemento:", menor)
print("Posição do menor elemento:", posicao)
