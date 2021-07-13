"""
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.

*Доработать скрипт: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""

import utils
import sys

if sys.argv[1:]:
    print('\nЗапуск из консоли\n')
    for el in sys.argv[1:]:
        date, cur_name, exchange_rate = utils.currency_rates(el)
        print(f'{cur_name}. Дата: {date}\nКурс перевода в рубли: {exchange_rate}\n')

else:
    print(utils.currency_rates('AUD'))

    print(utils.currency_rates('brl'))

    print(utils.currency_rates('Dkk'))