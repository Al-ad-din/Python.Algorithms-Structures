""" Задание № 1.
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы
с наиболее эффективным использованием памяти.
Примечание:
Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода
для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС."""

""" 
Разрядность ОС: 64-разрядная ОС, процессор x64, WINDOWS-10
Версия Python: 3.10.0 """

""" Берем для решения задание № 9 из урока № 3.
"Найти максимальный элемент среди минимальных элементов столбцов матрицы" """

print('Тест № 1')
import sys
import random

matrix = []

for i in range(15):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(15)])


min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('min_list')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print(
        'Максимальный элемент среди минимальных элементов столбцов матрицы: ',
        min_list[0]
            )

sum_size = 0
sum_size += sys.getsizeof(matrix)
sum_size += sys.getsizeof(min_list)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(string)
sum_size += sys.getsizeof(j)

print('Переменные занимают', sum_size)

print('===============================================================')
print('Тест № 2')

""" Берем для решения задание № 7 из урока № 3.
"В одномерном массиве целых чисел определить два наименьших элемента" """


import random
import sys

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')

print('Размер списка', sys.getsizeof(r))
print('Размер элемента списка', sys.getsizeof(r[0]))
print('Размер кортежа', sys.getsizeof(tuple(r)))
print('Размер элемента кортежа', sys.getsizeof(tuple(r)[0]))
sum = 0
for size in r:
    sum += sys.getsizeof(size)
print('Размер всех элементов в списке', sum)

# Размер списка больше, чем неизменяемый кортеж, с одним набором данных
# (912 байт у списка, 848 байт у кортежа).
# Размер зависит не от разрядности чисел, а от размера массива.
# Каждый элемент массива занимает 28 байт. 100 элементов по 28 байт занимают
# 2800 байт. Это значительно больше размера массива этих данных, т.к. Python
# делает оптимизацию и создаёт ссылки на один и тот же объект.