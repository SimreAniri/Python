"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""


class Car:
    __turn_direction = {'right': 'направо', 'left': 'налево'}

    def __init__(self, color, name, speed=0, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self, go_speed):
        print(f'Машина {self.name} тронулась со скоростью {go_speed}')
        self.speed = go_speed

    def stop(self):
        print(f'Машина {self.name} остановилась')
        self.speed = 0

    def turn(self, direction):
        print(f'Машина {self.name} повернула {self.__turn_direction[direction]}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name}: {self.speed}')


class TownCar(Car):
    def __init__(self, color, name, speed=0):
        super().__init__(color, name, speed)
        self.is_police = False

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!')


class SportCar(Car):
    def __init__(self, color, name, speed=0):
        super().__init__(color, name, speed)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color, name, speed=0):
        super().__init__(color, name, speed)
        self.is_police = False

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!')


class PoliceCar(Car):
    def __init__(self, color, name, speed=0):
        super().__init__(color, name, speed)
        self.is_police = True


pol = WorkCar('white', 1, 45)
print(pol.is_police)
pol.show_speed()
pol.stop()
pol.show_speed()
pol.go(55)
pol.turn('left')
