first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число : "))
third = int(input("Введите третье целое число: "))
if first == second == third:
    print(3)
if first == second or first == third or second == third:
    print(2)
elif first != second != third:
    print(0)
