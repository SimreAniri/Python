"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
>>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?

*Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и
возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Например:
>>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Сможете ли вы вернуть отсортированный по ключам словарь?
"""

def thesaurus(*lst, dct=dict()):
    word_dict = dct

    for i in lst:

        if i[0] in word_dict:
            word_dict[i[0]].append(i)

        else:
            word_dict[i[0]] = [i]

    word_dict = dict(sorted(word_dict.items(), key=lambda x: x[0]))

    for key in word_dict:
        word_dict[key].sort()

    return word_dict


def thesaurus_adv(*lst, dct=dict()):
    people_dict = dct

    for per in lst:
        name, surname = per.split()

        if surname[0] not in people_dict:
            people_dict[surname[0]] = {name[0]: [per]}

        else:
            if name[0] not in people_dict[surname[0]]:
                people_dict[surname[0]][name[0]] = [per]

            else:
                people_dict[surname[0]][name[0]].append(per)

    people_dict = dict(sorted(people_dict.items(), key=lambda x: x[0]))

    for key in people_dict:
        people_dict[key] = dict(sorted(people_dict[key].items(), key=lambda x: x[0]))

        for key2 in people_dict[key]:
            people_dict[key][key2].sort()

    return people_dict


new_dict = thesaurus("Иван", "Мария", "Петр", "Илья")
print(new_dict)

new_dict = thesaurus("Иас", "Марта", "Анна", "Стас", dct=new_dict)
print(new_dict)


new_dict2 = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(new_dict2)

new_dict2 = thesaurus_adv("Илья Северов", "Анна Скворцова", "Петр Мельников", "София Тюрина", "Инна Савельева", dct=new_dict2)
print(new_dict2)
