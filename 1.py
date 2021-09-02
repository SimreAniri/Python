"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class Color:
    __colors = {'red': '\033[0;31;49m',
                'yellow': '\033[0;33;49m',
                'green': '\033[0;32;49m',
                'end': '\033[0;0m'}

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return str(self.color)

    def print_text(self, text=None):

        if text:
            print(self.__colors[self.color] + text + self.__colors['end'])

        else:
            print(self.__colors[self.color] + self.color + self.__colors['end'])


class TrafficLight:
    __color_list = {'red': [7, 'yellow'], 'yellow': [2, 'green'], 'green': [10, 'red']}

    def __init__(self, color='red'):
        self.color = Color(color)

    def color_time(self):
        self.color.print_text()

        for i in range(self.__color_list[self.color.color][0]):
            self.color.print_text(str(i + 1))
            time.sleep(1)
        self.color = Color(TrafficLight.__color_list[self.color.color][1])

    def running(self, cycle_num=1):
        for _ in range(cycle_num):
            self.color_time()
            self.color_time()
            self.color_time()


light = TrafficLight()
light.running()
print(light.color)
light.color_time()
print(light.color)
# col = Color('red')
# print(col)
# col.print_text('hg')