"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""


duration = int(input("Введите время в секундах: "))

if duration < 60:
    print(f'{duration} сек')

elif duration < 60 * 60:
    print(f'{duration // 60} мин {duration % 60} сек')

elif duration < 60 * 60 * 24:
    print(f'{duration // (60 * 60)} час {duration % (60 * 60) // 60} мин {duration % (60 * 60) % 60} сек')

else:
    days = duration // (60 * 60 * 24)
    hours = duration % (60 * 60 * 24) // (60 * 60)
    minutes = duration % (60 * 60 * 24) % (60 * 60) // 60
    seconds = duration % (60 * 60 * 24) % (60 * 60) % 60

    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
