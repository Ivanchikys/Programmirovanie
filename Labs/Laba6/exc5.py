from random import randint

n = int(input('Введите количество строк:'))
m = int(input('Введите количество столбцов:'))

originalM = [[randint(1,9) for j in range(m)]  for i in range(n)]
rotatedM = [[[0] * n for i in range(n)] for j in range(m)] 

for i in range(n):   
    for j in range(m):    
        rotatedM[j][n-1-i] = originalM[i][j]

for row in  originalM: 
    print(' '.join([str(elem)for elem in row]))


for row in  rotatedM: 
    print(' '.join([str(elem)for elem in row]))