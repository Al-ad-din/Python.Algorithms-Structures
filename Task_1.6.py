''''Задание № 6.
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.'''

abc_number = int(input('Введите номер буквы в алфавите: '))

# Генерируем список букв английского алфавита
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(abc_list)
if abc_number <= len(abc_list):
    print(f'Буква под номером {abc_number}: {abc_list[abc_number - 1]}')
else:
    print(
      f'Введено число превышающее количество букв в алфавите ({len(abc_list)})'
    )