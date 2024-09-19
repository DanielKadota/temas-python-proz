
numero = int(input("Digite um número inteiro: "))

if numero > 1:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    
    if primo:
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")
else:
    print(numero, "não é um número primo.")

