# Inicializa as listas A e B com 5 elementos cada
A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]


print("Antes da troca:")
print("Lista A:", A)
print("Lista B:", B)


A, B = B, A


print("Depois da troca:")
print("Lista A:", A)
print("Lista B:", B)
