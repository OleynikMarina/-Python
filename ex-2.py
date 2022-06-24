class Road:
    def __init__(self, _width, _length, _weight, _depth):
        self.width = _width
        self.lenght = _length
        self.weight = _weight
        self.depth = _depth

    def result(self):
        print((self.width * self.lenght * self.weight * self.depth) // 1000)

res = Road(5000, 20, 25, 5)
res.result()
