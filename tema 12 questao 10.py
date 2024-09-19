numero = int(input("Digite um número entre 1 e 10: "))

if 1 <= numero <= 10:
    print("Tabuada do", numero, ":")
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)
else:
    print("Digite um valor entre 1 e 10.")
