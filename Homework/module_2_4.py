# "Всё не так уж просто"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    is_prime = True
    for j in range(1, numbers[i] - 1):
        if numbers[i] % numbers[j] == 0:
            is_prime = False
            break
        else:
            continue
    if is_prime:
        primes.append(numbers[i])
    elif not is_prime:
        not_primes.append(numbers[i])
print(f'Primes: {primes}')
print(f'Not_primes: {not_primes}')
