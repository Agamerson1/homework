from math import inf


def divide(first, second):
    result = 0
    result = first / second
    if second == 0:
        result = inf
    print(result)
    return inf


divide(10, 1)
