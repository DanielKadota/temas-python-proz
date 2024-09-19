# Lê a matriz
matriz = [[int(input("Digite o valor para a posição : ")) for j in range(5)] for i in range(5)]

# Calcula as somas
soma_linha_4 = sum(matriz[3])
soma_coluna_2 = sum(matriz[i][1] for i in range(5))
soma_diagonal_principal = sum(matriz[i][i] for i in range(5))
soma_diagonal_secundaria = sum(matriz[i][4 - i] for i in range(5))
soma_total = sum(sum(linha) for linha in matriz)

# Exibe as somas e a matriz
print("Matriz:")
for linha in matriz:
    print(linha)
print("Soma da linha 4:", soma_linha_4)
print("Soma da coluna 2:", soma_coluna_2)
print("Soma da diagonal principal:", soma_diagonal_principal)
print("Soma da diagonal secundária:", soma_diagonal_secundaria)
print("Soma total dos elementos:", soma_total)
