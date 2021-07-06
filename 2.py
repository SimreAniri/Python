"""
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

* (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place)
"""

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list)

i = 0

while i < len(my_list):

    if my_list[i].isdigit():
        my_list[i] = my_list[i].zfill(2)
        my_list.insert(i, '"')
        i += 1
        my_list.insert(i + 1, '"')

    elif (my_list[i].startswith('+') or my_list[i].startswith('-')) and my_list[i][1:].isdigit():
        my_list[i] = my_list[i][0] + my_list[i][1:].zfill(2)
        my_list.insert(i, '"')
        i += 1
        my_list.insert(i + 1, '"')

    i += 1

print(my_list)

my_str = ''
i = 0

while i < len(my_list):

    if my_list[i] == '"':
        my_str += ''.join(my_list[i: i+2 + 1])
        i += 2

    else:
        my_str += my_list[i]

    i += 1

    if i != len(my_list):
        my_str += ' '

print(my_str)
