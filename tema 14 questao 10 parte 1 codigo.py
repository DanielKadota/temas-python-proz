# main.py

from area_triangulo import calcular_area

# Lê a base e a altura do triângulo
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

# Calcula a área
area = calcular_area(base, altura)

# Exibe o resultado
print("A área do triângulo é:", area)
