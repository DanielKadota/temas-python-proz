# Lê o salário bruto
salario_bruto = float(input("Digite o salário bruto: "))

# Calcula a contribuição ao INSS
contribuicao_inss = salario_bruto * 0.11

# Salário líquido
salario_liquido = salario_bruto - contribuicao_inss

# Calcula o desconto do IRRF (exemplo: 15% do salário líquido)
irrf = salario_liquido * 0.15

# Exibe os resultados
print("Desconto do IRRF:", irrf)
