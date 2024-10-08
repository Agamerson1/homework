my_dict = {'Иван': 1999, 'Андрей': 2000, 'Маша': 2001}
print(my_dict)
print(my_dict['Андрей'])
print(my_dict.get('Даша'))
my_dict.update({'Руслан': 2002, 'Артём': 1998})
z = my_dict.pop('Маша')
print(z)
print(my_dict)
my_set = {1, 2, 1, 2, 1.5, 1.5}
print(my_set)
my_set.add(3)
my_set.add(7)
my_set.remove(1)
print(my_set)
