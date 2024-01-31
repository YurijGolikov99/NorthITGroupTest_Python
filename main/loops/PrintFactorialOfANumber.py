# Циклы: задание 4

"""
Пользователь вводит число.
Выводим в консоль факториал этого числа
"""

number = int(input("Введите число: "))

if number < 0:
    print("Факториал не может быть отрицательным!")
else:
    fact = 1

    for i in range(1, number+1):
        fact = fact * i

    print("Факториал числа ", number, " = ", fact)
