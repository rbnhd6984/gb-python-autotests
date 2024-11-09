

s = 12
p = 27
temp = s
# Введите ваше решение ниже
for i in range(s):
    if temp * i == p and i <= temp:
        print(f'{i} {temp}')
    temp -= 1
