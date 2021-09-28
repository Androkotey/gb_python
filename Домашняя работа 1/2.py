# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_time = 3779

hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
seconds = user_time % 60

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
