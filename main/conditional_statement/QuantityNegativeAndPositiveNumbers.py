# Условные операторы: задание 4

"""
Пользователь вводит в консоли четыре числа.
Рассчитываем и выводим в консоль количество отрицательных и положительных чисел
"""

print("Введите 4 числа: ")
number_one = float(input())
number_two = float(input())
number_three = float(input())
number_four = float(input())

positive_count = int(0)
negative_count = int(0)

positive_count = 0
negative_count = 0

if number_one > 0:
    positive_count += 1
elif number_one < 0:
    negative_count += 1

if number_two > 0:
    positive_count += 1
elif number_two < 0:
    negative_count += 1

if number_three > 0:
    positive_count += 1
elif number_three < 0:
    negative_count += 1

if number_four > 0:
    positive_count += 1
elif number_four < 0:
    negative_count += 1

print("Количество положительных чисел:", positive_count)
print("Количество отрицательных чисел:", negative_count)
