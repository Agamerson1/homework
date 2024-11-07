def divide(first, second):
    result = 0
    result = first / second
    if second == 0:
        result = 'Ошибка'
    print(result)
    return result


divide(10, 0)
