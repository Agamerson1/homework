my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
value = 0
while value < len(my_list):
    number = my_list[value]
    value = value + 1
    # print (number)
    if number == 0:
        continue
    elif number < 0:
        break
    print(number)  # встретилось отрицательное число- цикл закончился.