# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open("1.txt", 'w', encoding="utf-8") as data:
    while True:
        string_to_write = input("Введите строку для записи: ")
        if string_to_write:
            data.write(string_to_write + '\n')
        else:
            break
