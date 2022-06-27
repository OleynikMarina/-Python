class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')

res = Pen(Stationery)
res.draw()

res = Pencil(Stationery)
res.draw()

res = Handle(Stationery)
res.draw()

res = Stationery('"название канцелярской принадлежности"')
res.draw()
