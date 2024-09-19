def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

total_sum = 0
for num in range(1, 101):
    if is_prime(num):
        total_sum += num

print("A soma dos números primos entre 1 e 100 é:", total_sum)
