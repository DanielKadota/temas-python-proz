# Lê o salário bruto
salario_bruto = float(input("Digite o salário bruto: "))

# Calcula a contribuição ao INSS (exemplo: 11% do salário bruto)
contribuicao_inss = salario_bruto * 0.11

# Salário líquido
salario_liquido = salario_bruto - contribuicao_inss

# Exibe os resultados
print("Contribuição ao INSS:", contribuicao_inss)
print("Salário líquido:", salario_liquido)
