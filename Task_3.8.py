""" Задание № 8.
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу."""

matrix = []

for i in range(4):
    matrix.append([])
    sum = 0
    for n in range(4):
        user_number = int(input(f'Введите элемент {i+1} столбца {n+1}: '))
        sum += user_number
        matrix[i].append(user_number)

    matrix[i].append(sum)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))