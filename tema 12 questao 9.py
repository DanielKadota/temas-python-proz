# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Lê o peso e altura do usuário
while True:
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))
    
    if peso > 0 and altura > 0:
        break
    else:
        print("Peso e altura devem ser maiores que 0.")

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 24.9:
    classificacao = "Peso normal"
elif imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Exibe o resultado
print("Seu IMC é:", round(imc, 2))
print("Classificação:", classificacao)
