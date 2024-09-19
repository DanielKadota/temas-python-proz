def calcular_diferenca(valores):
    maior = max(valores)
    menor = min(valores)
    diferenca = maior - menor
    return diferenca

valores = []
n = int(input("Quantos valores você deseja inserir? "))

for i in range(n):
    valor = float(input("Digite o valor " + str(i+1) + ": "))
    valores.append(valor)

diferenca = calcular_diferenca(valores)

print("A diferença entre o maior e o menor elemento é: " + str(diferenca))