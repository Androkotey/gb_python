# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
        pass

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


employee_1 = Position("Vasya", "Pupkin", "ML-engineer", wage=100000, bonus=20000)
print(employee_1.name, employee_1.surname, employee_1.position)
print(employee_1._income)
print(employee_1.get_full_name())
print(employee_1.get_total_income())

employee_2 = Position("Leonid", "Agutin", "Analyst", wage=90000, bonus=15000)
print(employee_2.name, employee_2.surname, employee_2.position)
print(employee_2._income)
print(employee_2.get_full_name())
print(employee_2.get_total_income())
