# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите число: '))

max_digit = 0
while number > 0:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number //= 10

print(max_digit)
