
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o valor do desconto em %: "))
valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final com desconto: R$", round(preco_final, 2))
