def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

soma_primos = sum(i for i in range(1, 101) if eh_primo(i))
print("Soma dos números primos entre 1 e 100:", soma_primos)
