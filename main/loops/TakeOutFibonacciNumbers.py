# Циклы: задание 3

"""
Пользователь вводит число - х.
Выдаем число из последовательности фибоначчи с
индексом х
"""

x = int(input("Введите индекс числа из последовательности фибоначи: "))

if x < 0:
    print("Индекс не может быть отрицательным!")
else:
    previous = 0
    current = 1

    for i in range(2, x + 1):
        next_number = previous + current
        previous = current
        current = next_number

    print("число под индексом", x, ":", current)
