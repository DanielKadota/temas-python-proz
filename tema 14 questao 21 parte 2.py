# Lê um número inteiro
numero = input("Digite um número inteiro: ")

# Verifica se é palíndromo
if numero == numero[::-1]:
    print(numero, "é um número palíndromo.")
else:
    print(numero, "não é um número palíndromo.")
