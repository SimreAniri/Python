import sys
import os.path


with open('bakery.csv', 'r') as f:
    if len(sys.argv) == 1:
        print(f.read())

    elif len(sys.argv) == 2:
        if int(sys.argv[1]) <= os.path.getsize('bakery.csv') / 22:
            f.seek((int(sys.argv[1]) - 1) * 22)
            print(f.read())
        else:
            print('Таких записей не существует')

    elif len(sys.argv) == 3:
        if int(sys.argv[2]) <= os.path.getsize('bakery.csv') / 22:
            f.seek((int(sys.argv[1]) - 1) * 22)
            print(f.read((int(sys.argv[2]) - int(sys.argv[1]) + 1) * 21))
        else:
            print('Таких записей не существует')

    else:
        print('Ошибка в количестве аргументов')
