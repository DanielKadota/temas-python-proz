# Lê um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se é primo
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Exibe o resultado
if eh_primo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
