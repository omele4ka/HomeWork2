# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.

num = int(input('Введите количество чисел: '))
my_list = []
for i in range(1, num + 1):
    my_list.append((1 + 1/i) ** i)
print(my_list)
sum_elem = 0
for j in range(len(my_list)):
    sum_elem += my_list[j]
print(f'Сумма элементов списка {sum_elem}')
