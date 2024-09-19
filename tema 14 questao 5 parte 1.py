# Função para calcular dias de vida
def dias_de_vida(nome, idade):
    dias = idade * 365  # Considerando 365 dias por ano
    return nome + ", você já viveu aproximadamente " + str(dias) + " dias."

# Lê o nome do usuário
nome = input("Digite seu nome: ")

# Lê a idade do usuário
idade = int(input("Digite sua idade: "))

# Chama a função e armazena o resultado
resultado = dias_de_vida(nome, idade)

# Exibe o resultado
print(resultado)
