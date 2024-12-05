from pprint import pprint


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    number_str = 0
    byte_str = file.seek(0)
    for i in strings:
        file.write(f'{i}\n')
        number_str += 1
        key = (number_str, byte_str)
        string_positions[key] = i
        byte_str = file.tell()
    file.close()
    return string_positions


file_name = 'test.txt'
strings = ['Hello, World!', 'Привет, мир!', 'Bonjour, le monde!']
result = custom_write(file_name, strings)
pprint(result)
