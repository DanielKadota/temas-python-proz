hora = input("Digite a hora (HH:MM): ")
h, m = hora.split(':')
if 0 <= int(h) < 24 and 0 <= int(m) < 60:
    print("Hora válida.")
else:
    print("Hora inválida.")
