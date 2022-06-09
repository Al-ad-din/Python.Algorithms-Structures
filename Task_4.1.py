""" Задание № 1.
Проанализировать скорость и сложность одного любого алгоритма, разработанных
в рамках домашнего задания первых трех уроков.

Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их. """

import random
import timeit

"""
Для выполнения задания анализируем задание № 1 к уроку № 3 немного изменив условие:
"В диапазоне натуральных чисел от 2 до 100000 определить, 
сколько из них кратны любому из чисел в диапазоне от 2 до 100." """

def lst_generator_solution(lower, upper, devider_lower, devider_upper):
    print("Решение через сложный генератор списков в одну строку (полный перебор):",
          sum([(1 if sum(k) > 0 else 0) for k in
               [[(1 if (i % j == 0) else 0) for j in range(devider_lower, devider_upper)] for i in
                range(lower, upper)]]))

def normal_solution(lower, upper, devider_lower, devider_upper):
    n = 0
    for i in range(lower, upper):
        j = devider_lower
        while i % j != 0 and j <= devider_upper:
            j += 1
        n = (n + 1) if j <= devider_upper else n
    print("Обычный алгоритм проверки (перебор до первого деления без остатка):", n)


def optimal_solution(lower, upper, devider_lower, devider_upper):

    prime_lst = [2]
    for chek_num in range(prime_lst[0] + 1, devider_upper + 1):
        for i in prime_lst:
            if chek_num % i == 0: break
            if i == prime_lst[-1]: prime_lst.append(chek_num)

    n = 0
    for i in range(lower, upper):
        for j in prime_lst:
            if i % j == 0:
                n += 1
                break
    print("Оптимальный алгоритм проверки (перебор до первого деления без остатка):", n)


print("Расчет количества чисел в диапазоне от 2 до 100000 кратных хотя бы одному числу от 2 до 500")
print("Время расчета:", timeit.timeit("normal_solution(2, 100000, 2, 500)", setup="from __main__ import normal_solution", number=1), "\n")
print("Время расчета:", timeit.timeit("optimal_solution(2, 100000, 2, 500)", setup="from __main__ import optimal_solution", number=1), "\n")
print("Время расчета:", timeit.timeit("lst_generator_solution(2, 100000, 2, 500)", setup="from __main__ import lst_generator_solution", number=1))
print("\nВывод: При решении задачи через генератор списка код компактнее, но выполнение занимает много времени.\n"
      "Время выполнения задачи обычным перебором (до первого деления без остатка) в несколько раз дольше, чем выполнение оптимальным алгоритмом.\n"
      "Решение через сложный генератор списков в одну строку, занимает значительно дольше времени.")
