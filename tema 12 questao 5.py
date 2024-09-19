numeros_pares = []

while True: 
    numeros = int(input("Digite um numero: (Digite 0 para calcular) "))

    if numeros == 0: 
        break

    elif numeros % 2 == 0:
        numeros_pares.append(numeros)

print(numeros_pares)

somaDosPares = sum(numeros_pares)
print("Soma dos pares: ", somaDosPares)

quantidadeDePares = len(numeros_pares)
print("Quantidade dos pares: ", quantidadeDePares)

media = sum(numeros_pares) / len(numeros_pares)
print('A média: ',media)
