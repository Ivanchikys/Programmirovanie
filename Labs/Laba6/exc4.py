#Найдите индексы первого вхождения максимального элемента массива.
import numpy as np

n = int(input('Введите размер n(строк) = '))
m = int(input('Введите размер m(столбоцов) = '))

matrix = [
            [i * j for j in range(m)]
            for i in range(n)              ]

print(matrix)
