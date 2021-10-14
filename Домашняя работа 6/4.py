# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.potential_speed = speed
        self.speed = 0
        self.color = color
        self.name = name

    def go(self):
        self.speed = self.potential_speed
        print(f'Автомобиль {self.name} поехал.')

    def stop(self):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул в направлении: {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}')
        if self.speed > 60:
            print(f'Превышение максимально допустимой скорости на {self.speed-60} км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}')
        if self.speed > 40:
            print(f'Превышение максимально допустимой скорости на {self.speed-40} км/ч!')


class PoliceCar(Car):
    is_police = True

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)



print('Проверка TownCar')
t = TownCar(61, 'green', 'Town BMW')
print('Скорость', t.speed)
t.show_speed()
t.go()
print('Скорость', t.speed)
t.show_speed()
t.stop()
print('Скорость', t.speed)
t.show_speed()
print('=====================')
print('Проверка WorkCar')
w = WorkCar(70, 'yellow', 'Work Subaru')
print('Скорость', w.speed)
w.show_speed()
w.go()
print('Скорость', w.speed)
w.show_speed()
w.stop()
print('Скорость', w.speed)
w.show_speed()
print('=====================')
print('Проверка SportCar')
s = SportCar(120, 'red', 'Sport Maserati')
print('Скорость', s.speed)
s.show_speed()
s.go()
print('Скорость', s.speed)
s.show_speed()
s.stop()
print('Скорость', s.speed)
s.show_speed()
print('=====================')
print('Проверка PoliceCar')
p = PoliceCar(110, 'blue', 'Police Ferrari')
print('Скорость', p.speed)
p.show_speed()
p.go()
print('Скорость', p.speed)
p.show_speed()
p.stop()
print('Скорость', p.speed)
p.show_speed()
