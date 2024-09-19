soma = 0
count = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        soma += numero
        count += 1

media = soma / count if count > 0 else 0
print("Média dos números pares:", media)
