import sys
import os.path


with open('bakery.csv ', 'r+') as f:
    if len(sys.argv) == 3:

        if int(sys.argv[1]) > os.path.getsize('bakery.csv') / 22:
            print('Таких записей не существует')

        else:
            f.seek((int(sys.argv[1]) - 1) * 22)
            f.write(f'{sys.argv[2]:<20}\n')

    else:
        print('Неверное количество аргументов')


"""
Не совсем поняла, почему не работает с флагами a, a+
Заработало только с флагом r+

Объясните, пожалуйста в чем разница.
"""