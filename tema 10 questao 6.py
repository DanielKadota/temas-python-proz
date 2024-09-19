
def cifra_de_cesar(mensagem, chave):
    resultado = ""
    for caractere in mensagem:
        if caractere.isalpha():
            base = 65 if caractere.isupper() else 97
            resultado += chr((ord(caractere) - base + chave) % 26 + base)
        else:
            resultado += caractere
    return resultado

mensagem = input("Digite a mensagem a ser criptografada: ")
chave = int(input("Digite o valor da chave: "))

print("Mensagem criptografada:", cifra_de_cesar(mensagem, chave))
