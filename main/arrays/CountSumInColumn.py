# Массивы: задание 8

"""
Дан двумерный массив 5х5 с целыми числами.
Посчитать суммы чисел в каждом столбце и вывести наибольшую из них
"""

array = [[0] * 5 for _ in range(5)]

for row in range(len(array)):
    for col in range(len(array[row])):
        array[row][col] = row * len(array) + col + 1

max_column_sum = 0

for col in range(len(array[0])):
    column_sum = sum(row[col] for row in array)
    max_column_sum = max(max_column_sum, column_sum)

print("Наибольшая сумма в столбцах:", max_column_sum)
