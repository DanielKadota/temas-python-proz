rg = input("Digite o RG: ").replace(".", "").replace("-", "")
if len(rg) >= 9 and rg.isdigit():
    print("RG válido.")
else:
    print("RG inválido.")
