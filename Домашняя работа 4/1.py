# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv


def salary(num_hours, rate, award):
    return int(num_hours) * int(rate) + int(award)


try:
    assert len(argv) == 4
    print(salary(argv[1], argv[2], argv[3]))
except (AssertionError, ValueError):
    print('Введённые данные некорректны')
