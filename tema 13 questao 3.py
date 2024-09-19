nome = input("Digite um nome: ")
if nome.isalpha() and len(nome) > 0:
    print("Nome válido.")
else:
    print("Nome inválido.")
