class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}, {self.position}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {self._income["wage"] + self._income["bonus"]} руб.')

worker_marina = Position('Марина', 'Олейник', 'юрист', 30000, 20000)
worker_marina.get_full_name()
worker_marina.get_total_income()
