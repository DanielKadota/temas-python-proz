

from calculo_imc import calcular_imc

# Lê o peso e a altura do usuário
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Classifica o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Acima do peso"
else:
    classificacao = "Obesidade"

# Exibe o resultado
print(f"Seu IMC é: {imc:.2} - Classificação: {classificacao}")
