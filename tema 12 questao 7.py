genero = input("Digite as iniciais do seu genero:(M ou F)").upper()
print(genero)

while genero not in ['M', 'F']:    
    genero = input("Digite as iniciais do seu genero:(M ou F)").upper()

if genero == "M":
    print("Seu genero e masculino")
elif genero == "F":
    print("Seu genero e feminino")
