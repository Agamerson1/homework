calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    sttring = str(string)
    tuple = len(string), string.upper(), string.lower()
    count_calls()
    return tuple


def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            itog = True
            break
        else:
            itog = False
            continue
    return itog


print(string_info('Underground'))
print(string_info('downtown'))
print(is_contains('Logitech', ['tech', 'OgIgI', 'logITEcH']))
print(is_contains('master', ['remastered', 'cyclic', 'logitech']))
print(calls)
