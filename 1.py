"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError.

Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
"""
import re


def email_parse(email_address):
    pattern = re.compile(r'(?P<username>[A-z\.0-9]+)@(?P<domain>\w+\.\w+)')
    result = pattern.match(email_address)

    if result:
        return result.groupdict()

    raise ValueError(f'wrong email: {email_address}')


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
