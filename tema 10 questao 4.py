def soma_indices_pares(lista):
    soma = 0
    for i in range(0, len(lista), 2):
        soma +- lista[i]
    return soma
  
lista = [10, 20, 30, 40, 50, 60, 70]
resultado = soma_indices_pares(lista)
print("A soma dos elementos deindices pares é:", resultado)