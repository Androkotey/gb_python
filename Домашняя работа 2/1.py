# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

import array
from collections import deque

list_of_objects = [1, '2', [3, 4], (5, 6), {7: 8, 9: 10}, {11, 12}, None, True, array.array('i', [14, 15]),
                   frozenset((16, 17)), deque((18, 19)), print]

for element in list_of_objects:
    print(f'Элемент {element} имеет тип {type(element)}')
