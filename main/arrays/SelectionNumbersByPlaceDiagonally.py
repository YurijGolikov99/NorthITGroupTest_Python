# Массивы: задание 6

"""
Дан двумерный массив 10х10 с целыми числами.
Вывести в консоль все числа по диагонали от [0][0] до [10][10]
"""

array = [[0] * 10 for i in range(10)]

for row in range(len(array)):
    for col in range(len(array[row])):
        array[row][col] = row * len(array) + col + 1

for row in range(len(array)):
    for col in range(len(array[row])):
        if row == col:
            print(array[row][col], end=" ")
