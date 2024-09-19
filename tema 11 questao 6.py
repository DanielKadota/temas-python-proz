def calcular_inss(salario_bruto):
    # Tabela de alíquotas do INSS para 2024
    faixas = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (7786.02, 0.14)
    ]

    # Calcula a contribuição ao INSS
    contribuição = 0.0
    for faixa, aliquota in faixas:
        if salario_bruto > faixa:
            contribuição += faixa * aliquota
        else:
            contribuição += salario_bruto * aliquota
            break

    # Calcula o salário líquido
    salario_liquido = salario_bruto - contribuição

    return contribuição, salario_liquido

# Entrada do usuário
salario_bruto = float(input("Digite o valor do salário bruto: R$ "))

# Calcula a contribuição e o salário líquido
contribuição, salario_liquido = calcular_inss(salario_bruto)

# Exibe os resultados
print("Contribuição ao INSS: R$ " + str(round(contribuição, 2)))
print("Salário líquido: R$ " + str(round(salario_liquido, 2)))
