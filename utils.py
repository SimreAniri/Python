"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.

*Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

import requests
import datetime
from xml.etree import ElementTree


def currency_rates(code):
    api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    res = requests.get(api_url)

    tree = ElementTree.fromstring(res.content.decode('Windows-1251'))
    cur_date = datetime.datetime.strptime(tree.attrib['Date'], '%d.%m.%Y').date()

    for child in tree.findall('Valute'):

        for el in child:
            if el.tag == 'CharCode' and el.text == code.upper():

                return cur_date, child.find('Name').text, child.find('Value').text

    return

if __name__ =='__main__':

    # new_code = input('Введите код валюты: ')
    # date, cur_name, exchange_rate = currency_rates(new_code)
    #
    # print(f'{cur_name}.\nКурс перевода в рубли: {exchange_rate}')

    for cur in ['USD', 'EUR']:
        date, cur_name, exchange_rate = currency_rates(cur)
        print(f'{cur_name}. Дата: {date}\nКурс перевода в рубли: {exchange_rate}\n')

    print(type(date))
