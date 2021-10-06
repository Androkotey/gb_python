# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_data(name, surname, year, city, email, phone_number):
    """Выводит в консоль данные пользователя"""

    print(', '.join([name, surname, year, city, email, phone_number]))


user_data(name='Nikita', surname='Kotlyarov', year='1998', city='Saint-Petersburg',
          email='nikita.kotlyarov.2012@mail.ru', phone_number='8 800 555 35 35')
