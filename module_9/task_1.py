int_list = [6, 20, 15, 9]


def apply_all_functions(int_list, *functions):
    results = {}
    for function in functions:
        results.update({function.__name__: function(int_list)})
    return results


def min_(int_list):
    minimal = min(int_list)
    return minimal


def max_(int_list):
    maximal = max(int_list)
    return maximal


def len_(int_list):
    length = len(int_list)
    return length


def sum_(int_list):
    total = sum(int_list)
    return total


def sorted_(int_list):
    sorted_list = sorted(int_list)
    return sorted_list


def reverse_(int_list):
    reversed_list = int_list[::-1]
    return reversed_list


def reverse_sorted(int_list):
    sorted_list = sorted(int_list)
    reversed_sorted_list = sorted_list[::-1]
    return reversed_sorted_list


print(apply_all_functions(int_list, min_, max_, sum_, len_))
print(apply_all_functions(int_list, sorted_, reverse_sorted))
