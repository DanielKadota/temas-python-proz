# Lê a idade em anos, meses e dias
anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))

# Converte a idade para dias
total_dias = anos * 365 + meses * 30 + dias

# Exibe a idade em dias
print("Idade em dias:", total_dias)
