stroka = 'мо-локо и мёд'

stroka = stroka.split()
vowels = []
count = 0
for i in stroka:
    for j in i:
        if j in 'аеёиоуэюя':
            count += 1
    vowels.append(count)
    count = 0
if len(vowels) < 2:
    print("Количество фраз должно быть больше одной!")
elif len(set(vowels)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")


