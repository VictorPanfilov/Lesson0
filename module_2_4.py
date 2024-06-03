numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for x in numbers:
    if x < 2:
        continue
    is_prime = True
    # for i in range(2, x):
    # с точки зрения математики тут можно было бы написать
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(x)
    else:
        not_primes.append(x)
print('Primes:', primes)
print('Not Primes:', not_primes)
