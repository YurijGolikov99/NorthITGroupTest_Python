# Условные операторы: задание 6

"""
Пользователь вводит в консоли три числа.
Рассчитываем и выводим в консоль сумму наибольшего и наименьшего из них
"""

print("Введите 3 числа:")
number_one = int(input())
number_two = int(input())
number_three = int(input())

min_number = min(number_one, number_two, number_three)
max_number = max(number_one, number_two, number_three)

sum_result = min_number + max_number
print("Сумма наименьшего и наибольшего чисел:", sum_result)
