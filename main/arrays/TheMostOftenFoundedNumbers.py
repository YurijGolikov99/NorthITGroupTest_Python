# Массивы: задание 5

"""
Дан массив с целыми числами.
Вывести в консоль наиболее часто встречающееся.
Если таких несколько, то вывести наибольшее из них,
если повторяющихся нет, вывести соответствующее сообщение.
"""


array = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 8, 2]

frequency_dict = {}

for num in array:
    frequency_dict[num] = frequency_dict.get(num, 0) + 1

most_frequent = 0
max_frequency = 0

for key, value in frequency_dict.items():
    current_frequency = value
    if current_frequency > max_frequency or (current_frequency == max_frequency and key > most_frequent):
        most_frequent = key
        max_frequency = current_frequency

if max_frequency > 1:
    print("Наиболее часто встречающееся число:", most_frequent)
else:
    print("Нет повторяющихся чисел в массиве.")
