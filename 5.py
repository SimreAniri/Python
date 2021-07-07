"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random

def get_jokes(n, rep=True):
    """
    Создает n шуток
    :param n: количество шуток
    :param rep: повторять слова в разных шутках. По умолчанию в шутках слова могут повторяться
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = []

    if rep:
        for i in range(n):
            joke = ' '.join([random.choice(nouns), random.choice(adverbs), random.choice(adjectives)])
            jokes.append(joke)

    else:
        nouns = random.sample(nouns, n)
        adverbs = random.sample(adverbs, n)
        adjectives = random.sample(adjectives, n)

        for joke in zip(nouns, adverbs, adjectives):
            jokes.append(' '.join(joke))

    print(jokes)


get_jokes(2)
get_jokes(4)

print()

get_jokes(2, rep=False)
get_jokes(4, rep=False)

help(get_jokes)