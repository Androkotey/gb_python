# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class MyZeroDivisionError(Exception):
    def __init__(self, txt='\33[31mОшибка: Деление на 0.\33[0m'):
        self.txt = txt
        print(txt)


while True:
    a = input('Введите делимое: ')
    b = input('Введте делитель: ')
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            raise MyZeroDivisionError()
    except MyZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print(err)
    else:
        print('Результат:', a / b)
        break
