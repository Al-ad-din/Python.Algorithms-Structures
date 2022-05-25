""" Задание № 4. Определить, какое число в массиве встречается чаще всего."""

import random

num_list = [random.randint(1, 5) for _ in range(10)]
d = dict.fromkeys(num_list, 0)

for num in num_list:
    d[num] += 1

max_num = 0
for key in d:
    if d[key] > max_num:
        max_key = key
        max_num = d[key]

print(f'В заданном массиве \n{num_list} \nчаще всего ({max_num} раз) встречается число: {max_key}')