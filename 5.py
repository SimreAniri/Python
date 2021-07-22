"""
Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
* Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»)

Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
(должно быть 07 коп или 00 коп).

* Вывести цены, отсортированные по возрастанию, новый список не создавать
  (доказать, что объект списка после сортировки остался тот же).

* Создать новый список, содержащий те же цены, но отсортированные по убыванию.

* Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

product_price = [34.5, 67.78, 88.04, 123.8, 555.0, 527.8, 83, 23.764, 11.05, 9.99]

i = 0

for i, el in enumerate(product_price):

    print(f'{int(el)} руб {round(el % 1 * 100):02d} коп', end='')

    if i == len(product_price) - 1:
        print()

    else:
        print(', ', end='')


print("\nОтсортированный по возрастанию список")

for i, el in enumerate(sorted(product_price)):

    print(f'{int(el)} руб {round(el % 1 * 100):02d} коп', end='')

    if i == len(product_price) - 1:
        print()

    else:
        print(', ', end='')

print('Список: ', product_price, sep='\n')


print("\nОтсортированный по убыванию список")
sorted_product_price = sorted(product_price, reverse=True)

for i, el in enumerate(sorted_product_price):

    print(f'{int(el)} руб {round(el % 1 * 100):02d} коп', end='')

    if i == len(sorted_product_price) - 1:
        print()

    else:
        print(', ', end='')

print('Список: ', sorted_product_price, sep='\n')

print("\nСамые дорогие товары (5 шт.):")
print(sorted(product_price)[:5])
