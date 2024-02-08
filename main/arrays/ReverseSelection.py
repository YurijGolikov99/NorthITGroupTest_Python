# Массивы: задание 7

"""
Дан двумерный массив 10х10 с целыми числами.
Вывести в консоль все числа по диагонали от [0][10] до [10][0]
"""

array = [[0] * 10 for _ in range(10)]

for row in range(len(array)):
    for col in range(len(array[row])):
        array[row][col] = row * len(array) + col + 1

for row in range(len(array)):
    for col in range(len(array[row])):
        if row + col == len(array) - 1:
            print(array[row][col], end=" ")