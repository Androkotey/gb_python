# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


import random
from functools import reduce
from operator import add

with open('5.txt', 'w', encoding='utf-8') as f:
    print(*[random.randrange(100) for _ in range(15)], file=f)

with open('5.txt', 'r', encoding='utf-8') as f:
    numbers = f.read()

print(reduce(add, map(int, numbers.split())))
