# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.


""" Буду ждать разбора, чтобы посмотреть, как можно было сделать проще """


class Matrix:
    def __init__(self, input_data):
        self.data = input_data
        self._row_form = None
        self._meta_info = None

        if not self.__correct():
            print('Введена некорректная матрица')
            exit()

    def __correct(self) -> bool:
        if self.meta_info['type'] == 'scalar':
            try:
                int(self.data[0][0])
            except ValueError:
                return False
        else:
            length_of_row = len(self.data[0])
            for row in self.data:
                if len(row) != length_of_row:
                    return False
                for element in row:
                    try:
                        int(element)
                    except ValueError:
                        return False
        return True

    def __str__(self):
        padding = max([len(str(i)) for i in self.row_form])
        return '\n'.join(''.join(str(row[i]).rjust(padding + 2) if i > 0 else str(row[i]) for i in range(len(row))) for
                         row in self.data)

    @property
    def meta_info(self) -> dict:
        if self._meta_info is None:
            if len(self.data) == 1:
                if len(self.data[0]) == 1:
                    self._meta_info = {'type': 'scalar', 'shape': (1, 1)}
                else:
                    self._meta_info = {'type': 'vector', 'shape': (len(self.data[0]), 1)}
            else:
                self._meta_info = {'type': 'matrix', 'shape': (len(self.data[0]), len(self.data))}
        return self._meta_info

    @property
    def row_form(self):
        if self._row_form is None:
            if self._meta_info['type'] == 'scalar':
                return self.data[0]
            data = []
            for row in self.data:
                for element in row:
                    data.append(element)
            self._row_form = data
        return self._row_form

    def _matrix_form(self, row_form):
        num_of_columns = self.meta_info['shape'][0]
        num_of_rows = self.meta_info['shape'][1]

        data = []
        i = 0
        while i < num_of_columns * num_of_rows:
            new_row = row_form[i:i + num_of_columns]
            i += num_of_columns
            data.append(new_row)

        return data

    def __add__(self, other):
        if self.meta_info != other.meta_info:
            print('Данные матрицы сложить нельзя!')
            return None

        row = [i + j for i, j in zip(self.row_form, other.row_form)]
        return Matrix(self._matrix_form(row))


m1 = Matrix([[1, 2, 1], [2, 1, 2], [1, 2, 1]]) + Matrix([[2, 1, 2], [0, 5, 0], [1, 1, 1]])
print(m1)
m2 = Matrix([[1]]) + Matrix([[2, 4]])
