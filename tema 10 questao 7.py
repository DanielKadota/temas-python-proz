#armazenamento de numeros
numeros = [1.0,5.6, 7.8, 0.2,4.6]

menor_valor = float('inf')
indice_menor_valor = -1

for i in range(len(numeros)):
   if numeros[i] < menor_valor:
        menor_valor = numeros[i]
        indice_menor_valor = i

print("O menor valor da lista é", menor_valor, "e está na posição", indice_menor_valor, ".")