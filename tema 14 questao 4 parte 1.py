# Função para calcular o pagamento
def pagamento(horas_trabalhadas, valor_hora):
    return horas_trabalhadas * valor_hora

# Lê as horas trabalhadas
horas = float(input("Digite as horas trabalhadas: "))

# Lê o valor por hora
valor = float(input("Digite o valor por hora: "))

# Chama a função e armazena o resultado
valor_a_pagar = pagamento(horas, valor)

# Exibe o valor a ser pago
print("Valor a ser pago: R$", valor_a_pagar)
