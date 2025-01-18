int_list = [6, 20, 15, 9]

def apply_all_functions(int_list, *functions):
    results = {}
    for function in functions:
        results.update({function.__name__: function(int_list)})
    return results


print(apply_all_functions(int_list, min, max, sum))
print(apply_all_functions(int_list, sorted, len))
