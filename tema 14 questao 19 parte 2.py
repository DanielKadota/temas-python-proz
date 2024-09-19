# Menu de opções
print("Escolha a conversão:")
print("1. Centímetros para Polegadas")
print("2. Polegadas para Centímetros")
print("3. Quilômetros para Milhas")
print("4. Milhas para Quilômetros")

opcao = int(input("Digite o número da opção: "))

valor = float(input("Digite o valor a ser convertido: "))

if opcao == 1:
    resultado = valor * 0.3937
elif opcao == 2:
    resultado = valor * 2.54
elif opcao == 3:
    resultado = valor * 0.6214
elif opcao == 4:
    resultado = valor * 1.6093
else:
    resultado = "Opção inválida."

# Exibe o resultado
print("Resultado:", resultado)
