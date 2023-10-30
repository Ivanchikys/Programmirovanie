#Найдите индексы первого вхождения максимального элемента массива.
import numpy as np

n = int(input('Введите размер n(строк) = '))
m = int(input('Введите размер m(столбоцов) = '))
#matrix = [[1,2,8],[4,2,1],[5,2,8]]
matrix = [
            [i * j for j in range(m)]
            for i in range(n) 
         ]

print(matrix)

max = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        #print(matrix[i][j])       (работа цикла ⬆)
        if matrix[i][j] > max:
            max = matrix[i][j]
            max_i, max_j = i , j

print(max_i ,' ', max_j)