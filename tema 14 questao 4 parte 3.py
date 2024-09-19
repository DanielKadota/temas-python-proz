# Lê a mensagem e a chave
mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave: "))
criptografada = ""

# Criptografa a mensagem
for char in mensagem:
    if char.isalpha():
        deslocamento = ord(char) + chave
        if char.islower() and deslocamento > ord('z'):
            deslocamento -= 26
        elif char.isupper() and deslocamento > ord('Z'):
            deslocamento -= 26
        criptografada += chr(deslocamento)
    else:
        criptografada += char

# Exibe a mensagem criptografada
print("Mensagem criptografada:", criptografada)
