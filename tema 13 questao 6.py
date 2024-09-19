data = input("Digite a data (DD/MM/AAAA): ")
dia, mes, ano = data.split('/')
if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12:
    print("Data válida.")
else:
    print("Data inválida.")
