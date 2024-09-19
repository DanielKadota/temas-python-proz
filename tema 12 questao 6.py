numeros = []

while True:
    valores = int(input("Digite um numero:(digite 0 para calcular): "))

    if valores == 0:
        break

    numeros.append(valores)

menor_numero = min(numeros)
maior_numero = max(numeros)

print("Menor numero: " ,menor_numero)
print("Maior numero: " , maior_numero)
