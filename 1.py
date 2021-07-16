"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
*Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


print(odd_nums(3))

od_to_5 = (i for i in range(1, 5 + 1, 2))
print(od_to_5)
print(next(od_to_5))
print(next(od_to_5))
print(next(od_to_5))
print(next(od_to_5))