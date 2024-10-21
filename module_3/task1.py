from xmlrpc.client import boolean

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
    string = string.lower
    list_to_search = list(list_to_search)
    for i in list_to_search:
        if list_to_search == string:
            boolean = True
            break
        else:
            boolean = False
            continue
    count_calls()


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
