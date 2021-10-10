# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# 7.txt:
"""
firm_1 ООО 10000 5000
firm_2 ОAО 20000 10000
firm_3 ОAО 30000 5000
firm_4 ООB 40000 50000
firm_5 ООО 15000 1000
"""
import json

firms = [dict(), {'average_profit': 0}]
sum_profit = 0
firms_with_profit = 0
with open('7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        firm, _, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms[0][firm] = profit
        if profit > 0:
            sum_profit += profit
            firms_with_profit += 1
firms[1]['average_profit'] = sum_profit // firms_with_profit

with open('7.json', 'w', encoding='utf-8') as file:
    json.dump(firms, file)
