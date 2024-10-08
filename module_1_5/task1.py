immutable_var = 1, True, "moonlight", 10.1
print(immutable_var)
# immutable_var [0] = 3  #Кортеж- неизменяемая упорядоченная коллекция, включающая в себя разные типы данных.'tuple' object does not support item assignment.
# print(immutable_var)
mutable_list = [2, False, "sunlight"]
mutable_list[0] = 1000
print(mutable_list)
