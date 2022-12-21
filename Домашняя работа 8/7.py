# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
from itertools import combinations


class ComplexNumber:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        sign = '+' if self.im >= 0 else '-'
        return f"{self.re}{sign}{abs(self.im)}j"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(re=self.re + other.re, im=self.im + other.im)
        else:
            if isinstance(other, int) or isinstance(other, float):
                return ComplexNumber(re=self.re + other, im=self.im)

    def __radd__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(re=self.re + other.re, im=self.im + other.im)
        else:
            if isinstance(other, int) or isinstance(other, float):
                return ComplexNumber(re=other + self.re, im=self.im)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(re=self.re - other.re, im=self.im - other.im)
        else:
            if isinstance(other, int) or isinstance(other, float):
                return ComplexNumber(re=other - self.re, im=self.im)

    def __rsub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(re=self.re - other.re, im=self.im - other.im)
        else:
            if isinstance(other, int) or isinstance(other, float):
                return ComplexNumber(re=other - self.re, im=self.im)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            re = self.re * other.re - self.im * other.im
            im = self.re * other.im + self.im * other.re
            return ComplexNumber(re, im)
        else:
            return ComplexNumber(self.re * other, self.im * other)

    def __rmul__(self, other):
        if isinstance(other, ComplexNumber):
            re = self.re * other.re - self.im * other.im
            im = self.re * other.im + self.im * other.re
            return ComplexNumber(re, im)
        else:
            return ComplexNumber(self.re * other, self.im * other)


i1 = ComplexNumber(2, -3)
i2 = ComplexNumber(0, 6)
i3 = 2
i4 = ComplexNumber(10, -10)
i5 = ComplexNumber(-2, 0)

list_of_numbers = [i1, i2, i3, i4, i5]
for num_1, num_2 in combinations(list_of_numbers, 2):
    print(f'({num_1}) + ({num_2}) = {num_1 + num_2}')
    print(f'({num_2}) + ({num_1}) = {num_2 + num_1}')
    print(f'({num_1}) - ({num_2}) = {num_1 - num_2}')
    print(f'({num_2}) - ({num_1}) = {num_2 - num_1}')
    print(f'({num_1}) * ({num_2}) = {num_1 * num_2}')
    print(f'({num_2}) * ({num_1}) = {num_2 * num_1}')

print('Сумма чисел в списке: ', sum(list_of_numbers))
