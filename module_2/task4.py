numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if i < 2:
        continue
    is_prime = True
    # print(i)
    if i % 1 == 0 and i % i == 0 and i % 2 != 0 and i % 15 != 0:
        primes.append(i)
    else:
        if not (is_prime):
            not_primes.append(i)
print(primes)
print(not_primes)
