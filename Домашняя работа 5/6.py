# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

# 6.txt:
"""
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
"""

subject_dict = dict()
with open('6.txt', 'r', encoding='utf-8') as file:
    for raw_line in file:
        prepared_line = raw_line.split()
        subject_dict[prepared_line[0][:-1]] = 0
        for raw_element in prepared_line:
            prepared_element = raw_element.split('(')
            try:
                subject_dict[prepared_line[0][:-1]] += int(prepared_element[0])
            except ValueError:
                continue

print(subject_dict)
