# Números pares
pares = [(10, 2),(6,2),(15,3)]

# Laço de repetição
for par in pares:
    a, b = par
    i = 0
    while a > b:
        a -= b
        i += 1
    print("Para os números", par[0],"e", par[1],":")
    print("Valor final de A:", a)
    print("Valor final de C:", i)
