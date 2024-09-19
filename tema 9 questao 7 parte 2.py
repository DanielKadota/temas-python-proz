
valor = int(input("Digite o valor da conta: "))

notas_50 = valor // 50
valor %= 50
notas_10 = valor // 10
valor %= 10
notas_1 = valor

print("Notas de 50:", notas_50)
print("Notas de 10:", notas_10)
print("Notas de 1:", notas_1)
