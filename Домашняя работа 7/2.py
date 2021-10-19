# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import abstractmethod, ABC


class Clothes(ABC):
    total_material = 0

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def material(self):
        pass


class Coat(Clothes):
    total_material = 0

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        self._material = self.material
        # наверное проще было бы подсчёт расхода материала производить сразу при инициализации, но по заданию надо
        # использовать @property. Не совсем ясна необходимость его использования в данном задании.

    @property
    def material(self):
        self._material = self.size / 6.5 + 0.5
        Coat.total_material += self._material
        Clothes.total_material += self._material
        return self._material


class Suit(Clothes):
    total_material = 0

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
        self._material = self.material

    @property
    def material(self):
        self._material = self.height * 2 + 0.3
        Suit.total_material += self._material
        Clothes.total_material += self._material
        return self._material


coat_1 = Coat('coat_1', 30)
coat_2 = Coat('coat_2', 50)
suit_1 = Suit('suit_1', 1.9)
suit_2 = Suit('suit_2', 1.8)
print(Clothes.total_material)
