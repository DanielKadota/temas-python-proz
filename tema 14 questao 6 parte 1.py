def converter_data(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    try:
        dia, mes, ano = map(int, data.split('/'))
        if 1 <= dia <= 31 and 1 <= mes <= 12:
            return str(dia) + " de " + meses[mes - 1] + " de " + str(ano)
    except ValueError:
        return None
    return None

data_input = input("Digite uma data no formato DD/MM/AAAA: ")
resultado = converter_data(data_input)

if resultado:
    print(resultado)
else:
    print("Data inválida.")
