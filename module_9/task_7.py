def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        if x % x == 0 and x % 1 == 0 and x % 2 != 0:
            result = 'Простое'
        else:
            result = 'Составное'
        print(result)
        return x

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(4, 3, 6)
print(result)
