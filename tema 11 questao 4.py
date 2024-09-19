
numero = int(input("Digite um número inteiro: "))


soma = 0


for i in range(1, numero + 1):
    if i % 2 == 0:
        soma += i


print("A soma dos números pares entre 1 e {numero} é: {soma}")

    
