# Условные операторы: задание 1

"""
Пользователь вводит в консоли число.
Если оно больше 10, выдаем в консоли сообщение “Число больше десяти”,
если меньше – “Число меньше десяти”
"""

enter_number = int(input("Введите число: "))

if enter_number > 10:
    print("Число больше десяти.")
elif enter_number < 10:
    print("Число меньше десяти.")
else:
    print("Число равно десяти.")
