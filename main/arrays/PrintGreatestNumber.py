# Массивы: задание 4

"""
Дан массив с целыми числами.
Вывести в консоль наибольшее из них
"""

array = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11]

maxNumber = array[0]

for num in array:
    if num > maxNumber:
        maxNumber = num;

print("Наибольший элемент в массиве: ", maxNumber)
