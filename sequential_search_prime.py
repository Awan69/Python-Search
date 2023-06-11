def prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def cari_nomer_prima(numbers):
    prime_numbers = []
    for num in numbers:
        if prima(num):
            prime_numbers.append(num)
    return prime_numbers


numbers = [7, 10, 13, 6, 17, 22, 19]


prime_numbers = cari_nomer_prima(numbers)


print("Bilangan prima dalam daftar:", prime_numbers)
