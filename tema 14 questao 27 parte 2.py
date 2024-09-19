maior = None
menor = None

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

print("Maior número:", maior)
print("Menor número:", menor)
