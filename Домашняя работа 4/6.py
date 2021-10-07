# 6. Реализовать два небольших скрипта.

from itertools import count, cycle

# а) Итератор, генерирующий целые числа, начиная с указанного.


def gen_int(start=0):
    assert start >= 0
    stop = start + 10

    for i in count(start):
        if i > stop:
            return
        print(i)


gen_int(0)

# б) Итератор, повторяющий элементы некоторого списка, определенного заранее.


def gen_cycle(iter_obj):
    stop = 3*len(iter_obj)

    for i, obj in enumerate(cycle(iter_obj)):
        if i == stop:
            return
        print(obj)


gen_cycle('ABC')
