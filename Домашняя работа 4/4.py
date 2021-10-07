# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

import time
import random

my_list = [random.randint(0, 1500) for _ in range(10000)]

# Варимант 1 (сложность O(n))
start = time.perf_counter()

repeated_values = set()
unique_values = set()

for value in my_list:
    if value in repeated_values:
        continue
    if value in unique_values:
        unique_values.discard(value)
        repeated_values.add(value)
        continue
    unique_values.add(value)

print([i for i in my_list if i in unique_values])
end = time.perf_counter()

print(f'Время работы первого варианта: {end - start}')

# Вариант 2 (сложность O(n^2))
start = time.perf_counter()

print([i for i in my_list if my_list.count(i) == 1])
end = time.perf_counter()

print(f'Время работы второго варианта: {end - start}')
