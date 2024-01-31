# Условные операторы: задание 5

"""
Пользователь вводит в консоли три числа, выводим самое большое из них.
"""

print("Введите 3 числа:")
number_one = int(input())
number_two = int(input())
number_three = int(input())

if number_one >= number_two and number_one >= number_three:
    print("Самое большое число: ", number_one)
elif number_two >= number_one and number_two >= number_three:
    print("Самое большое число: ", number_two)
else:
    print("Самое большое число: ", number_three)
