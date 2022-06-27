class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print('Машина поехала')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self, direction='прямо'):
        direction = direction.lower()
        if direction == 'прямо':
            print(f'Автомобиль {self.name} движется по прямой')
        elif direction == 'направо':
            print(f'Автомобиль {self.name} повернул направо')
        elif direction == 'налево':
            print(f'Автомобиль {self.name} повернул налево')
        elif direction == 'назад':
            print(f'Автомобиль {self.name} повернул в обратном направлении')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Предупреждение: превышение скорости!')

class SportCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость автомобиля: {self.speed} км/ч')
            print('Предупреждение: превышение скорости!')

class PoliceCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')

res = WorkCar(90, 'красный', 'WorkCar', False)
res.go()
res.stop()
res.turn('налево')
res.show_speed()
