#Нужно задать числовой список. В этом списке n = 5 строк, m = 6 столбцов, и элемент в строке i и столбце j вычисляется по формуле: a[i][j] = i * j.
n , m = 5 , 6

matrix = [
            [i * j for j in range(m)]
            for i in range(n)              ]
#print(matrix)

for line in matrix:
    print(' '.join([str(element) for element in line]))