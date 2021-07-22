"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

* Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

import os
import json

ROOT_DIR = 'G:\Программирование\_Разработчик Python\I четверть\Основы языка Python\Python\some_data'

size_cont_dict = dict()

for el in os.scandir(ROOT_DIR):
    size = el.stat().st_size
    len_size = len(str(size))
    key_dict = int('1'+'0'*len_size)

    if key_dict not in size_cont_dict:
        size_cont_dict[key_dict] = [0, []]

    size_cont_dict[key_dict][0] += 1

    el_type = el.name.split('.')[1]
    if el_type not in size_cont_dict[key_dict][1]:
        size_cont_dict[key_dict][1].append(el_type)

size_cont_dict = {x: (size_cont_dict[x][0], size_cont_dict[x][1]) for x in size_cont_dict}
print(size_cont_dict)

with open(os.path.join(os.path.dirname(__file__), f'{os.path.basename(ROOT_DIR)}_summary.json'), 'w', encoding='utf-8') as f:
    json.dump(size_cont_dict, f, indent=4)
    print('Файл сохранен')
