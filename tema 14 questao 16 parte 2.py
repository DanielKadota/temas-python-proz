# Lê um número par do usuário
numero = int(input("Digite um número par: "))

# Calcula a soma dos números pares
soma = sum(i for i in range(0, numero + 1, 2))

# Exibe a soma
print("A soma dos números pares é:", soma)
