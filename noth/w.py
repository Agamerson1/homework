kubatura6 = {30: 0.52, 32: 0.59, 34: 0.66, 36: 0.74, 38: 0.82, 40: 0.9, 42: 1, 44: 1.09, 46: 1.19, 48: 1.3, 50: 1.41,
             52: 1.53, 54: 1.65, 56: 1.78, 58: 1.91, 60: 2.05, 62: 2.18, 64: 2.32, 66: 2.44, 68: 2.57}
total_kubatura = 0
for diameter, kubatura6 in kubatura6.items():
    count = int(input(f"Количество брёвен диаметром {diameter} см: "))
    total_kubatura += count * kubatura6

print(f"Кубатура: {total_kubatura} куб. м")
print('Зарплата- ', total_kubatura * 300)
