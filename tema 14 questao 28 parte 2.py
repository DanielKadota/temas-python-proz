sexo = input("Digite o sexo (M/F): ").upper()
while sexo not in ['M', 'F']:
    sexo = input("Valor inválido. Digite M ou F: ").upper()

print("Sexo informado:", sexo)
