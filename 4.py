"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""
from functools import wraps


def val_checker(val):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            res = func(*args)

            if val(*args):
                return res

            raise ValueError(f'wrong val {args}')

        return wrapper
    return _val_checker




@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


@val_checker(lambda x, y: x > 0 and y > 0)
def calc_func(x, y):
    return x ** 3 + y


print(calc_cube(5))

help(calc_func)

print(calc_func(5, -4))
