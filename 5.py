"""
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""

from collections import Counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_counts = Counter(src)

print(src_counts)

src_unique = [num for num in src if src_counts[num] == 1]
print(src_unique)