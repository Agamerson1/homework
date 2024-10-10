grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # в алфавитном порядке Aaron Bilbo Johnny Khendrik Steve
names = list(students)  # переменная имён студентов во множестве
names.sort()  # сортировка списка студентов по именам в алфавитном порядке
gpa = {}
gpa.update({names[0]: sum(grades[0]) / len(grades[0]), names[1]: sum(grades[1]) / len(grades[1]),
            names[2]: sum(grades[2]) / len(grades[2]), names[3]: sum(grades[3]) / len(grades[3]),
            names[4]: sum(grades[4]) / len(grades[4])})
print(gpa)