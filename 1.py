"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
>>> >>> num_translate("one")
"один"

Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.

* (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
>>> >>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""

def num_translate(num):
    num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                'nine': 'девять', 'ten': 'десять'}

    if num.lower() not in num_dict:
        return

    else:
        if num.istitle():
            return num_dict[num.lower()].title()

        elif num.islower():
            return num_dict[num]

        else:
            print('Проверьте регистр букв. Заглавной может быть только первая.')
            cor_num = input('Введите число на английском:')
            return num_translate(cor_num)


your_num = input('Введите число на английском:')
print(num_translate(your_num))
