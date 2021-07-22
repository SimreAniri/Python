"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая.

Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах превышает объём ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи

* Реализовать интерфейс командной строки, чтобы можно было задать путь к обоим исходным файлам и путь к выходному
файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
"""

import sys
import json


hobby_dict = dict()

if sys.argv[1:]:
    if len(sys.argv) == 3:
        users_file = sys.argv[1]
        hobby_file = sys.argv[2]
    else:
        print('Неверное число аргументов. Введите 2 файла для анализа.')
        users_file = input('Пользователи: ')
        hobby_file = input('Хобби: ')

else:
    users_file = 'users.csv'
    hobby_file = 'hobby.csv'

with open(users_file, 'r') as users, open(hobby_file, 'r') as hobby:
    for user in users:
        user = ' '.join(user.strip().split(','))

        if user not in hobby_dict:
            hobby_dict[user] = []

        hobby_list = hobby.readline()

        if hobby_list:
            hobby_dict[user].extend(hobby_list.strip().split(','))

        else:
            hobby_dict[user] = None

    hobby_list = hobby.readline()

    if hobby_list:
        sys.exit(1)

print(hobby_dict)

with open('hobby_dict.json', 'w') as f:
    json.dump(hobby_dict, f, ensure_ascii=False)
