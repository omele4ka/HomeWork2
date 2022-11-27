# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random
my_list = []
for i in range(5):
    my_list.append(i)
print(f'Исходный список {my_list}')

def shuffle_elem(original_list):
    new_list = original_list[:]
    new_list_length = len(new_list)
    for i in range(new_list_length):
        new_list_index = random.randint(0, new_list_length - 1)
        temp = new_list[i]
        new_list[i] = new_list[new_list_index]
        new_list[new_list_index] = temp
    return new_list
print(f'Новый список {shuffle_elem(my_list)}')


