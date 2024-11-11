def calculate_structure_sum(data_structure):
    summ = 0
    for i in data_structure:
        if isinstance(i, int):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, int):
                    summ += key
                elif isinstance(key, str):
                    summ += len(key)
                if isinstance(value, int):
                    summ += value
                elif isinstance(value, str):
                    summ += len(value)
                elif isinstance(value, (list, tuple, set, dict)):
                    summ += calculate_structure_sum([value])
    return summ


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)

print(result)
