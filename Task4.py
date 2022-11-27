# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

import random
my_list = []
for i in range(1, 6):
    my_list.append(random.randint(1000, 9999))
print(f'Рандомный список элементов: {my_list}')

num_to_delete = input('Введите цифру: ')
for i in range(len(my_list)):
    my_list[i] = int(str(my_list[i]).replace(num_to_delete, ''))
print(f'Список без цифры {num_to_delete} - {my_list}')

def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    while sum > 9:
        sum = sum % 10 + sum // 10
    return sum
for i in range(len(my_list)):
    my_list[i] = sum_digits(my_list[i])
print(f'Сумма цифр в элементах списка: {my_list}')

final_list = []
for i in range(len(my_list)):
    if my_list[i] not in final_list:
        final_list.append(my_list[i])
print(f'Финальный список элементов: {final_list}')
