
email = input("Digite um e-mail: ")
if re.match(r'^[\w\.-]+@\w+\.\w+$', email):
    print("E-mail válido.")
else:
    print("E-mail inválido.")
