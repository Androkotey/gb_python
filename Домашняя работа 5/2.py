# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# 2.txt:
"""
They rode off towards the sunset. Behind them they left a darkening valley.
Behind them was a lake, an enchanted lake, a lake blue and smooth as a polished sapphire.
Behind them were left the boulders littering the shore. And pine trees on the slope.

That was left behind them.
And everything else was in front of them.
"""


with open("2.txt", "r", encoding="utf-8") as file:
    strings_from_file = file.readlines()
    print(f'Строк в файле: {len(strings_from_file)}')

    for i, string in enumerate(strings_from_file):
        print(f'В строке {i+1} количество слов: {len(string.split())}')
