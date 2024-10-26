kubatura6 = {30: 0.52, 32: 0.59, 34: 0.66, 36: 0.74, 38: 0.82, 40: 0.9, 42: 1, 44: 1.09, 46: 1.19, 48: 1.3, 50: 1.41,
             52: 1.53, 54: 1.65, 56: 1.78, 58: 1.91, 60: 2.05, 62: 2.18, 64: 2.32, 66: 2.44, 68: 2.57}
total_kubatura = 0
for diameter6, kubatura in kubatura6.items():
    count = int(input(f"Количество 6м брёвен диаметром {diameter6} см: "))
    total_kubatura += count * kubatura6

print(f"Кубатура: {total_kubatura} куб. м")
print('Зарплата- ', total_kubatura * 300)

kubatura4 = {34: 0.43, 36: 0.48, 38: 0.53, 40: 0.58, 42: 0.64, 44: 0.7, 46: 0.77, 48: 0.84, 50: 0.91, 52: 0.99,
             54: 1.07, 56: 1.16, 58: 1.25, 60: 1.33, 62: 1.43, 64: 1.52, 66: 1.61, 68: 1.7}
sum = 0
for diameter4, kubatura in kubatura4.items():
    count1 = int(input(f"Количество 4м брёвен диаметром {diameter4} см: "))
    sum += count1 * kubatura4
