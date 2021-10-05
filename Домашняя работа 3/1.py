# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(dividend, divider):
    """ Возвращает частное делимого (первый аргумент) и делителя (второй аргумент) """

    try:
        quotient = dividend / divider
    except ZeroDivisionError:
        return
    return quotient


a, b = map(int, input('Введите делимое и делитель через пробел: ').split())
print(division(a, b))
