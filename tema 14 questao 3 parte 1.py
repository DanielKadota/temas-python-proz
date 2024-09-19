# Função para somar dois números
def soma(a, b): 
    return a + b

# Função para subtrair o segundo número do primeiro
def subtracao(a, b): 
    return a - b

# Função para multiplicar dois números
def multiplicacao(a, b): 
    return a * b

# Função para dividir o primeiro número pelo segundo
# Verifica se o divisor não é zero
def divisao(a, b): 
    return a / b if b != 0 else "Divisão por zero não é permitida."

# Lê o primeiro número inteiro
num1 = int(input("Digite o primeiro número: "))

# Lê o segundo número inteiro
num2 = int(input("Digite o segundo número: "))

# Exibe o resultado da soma
print("Soma:", soma(num1, num2))

print("Subtração:", subtracao(num1, num2))

print("Multiplicação:", multiplicacao(num1, num2))

print("Divisão:", divisao(num1, num2))
