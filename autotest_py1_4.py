import random

list_length = random.randint(7, 10)

random_numbers_list = [random.randint(1, 15) for _ in range(list_length)]

unique_numbers_list = []
[unique_numbers_list.append(i) for i in random_numbers_list if i not in unique_numbers_list]
print(random_numbers_list)
print(unique_numbers_list)

