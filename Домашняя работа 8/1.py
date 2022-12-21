# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date: str):
        self.date = Date.date_to_number(date)
        if not self.validate(self.date):
            raise ValueError

    @staticmethod
    def validate(date):
        day_condition = 1 <= date['day'] <= 31
        month_condition = 1 <= date['month'] <= 12
        year_condition = 1901 <= date['year'] <= 2099
        return day_condition and month_condition and year_condition

    @classmethod
    def date_to_number(cls, date):
        day, month, year = map(int, date.split('-'))
        return {'day': day, 'month': month, 'year': year}


date_1 = Date('11-12-2023')
print(date_1.date)
date_2 = Date('01-12-2023')
print(date_2.date)
date_3 = Date('11-02-2023')
print(date_3.date)
date_4 = Date('11-12-1950')
print(date_4.date)
date_5 = Date('11-13-2023')
