
#n = int(input('Введите кол-во строк: '))
#m = int(input('Введите кол-во столбцов: '))

#matrix = [
            #[i * j for j in range(m)]
            #for i in range(n)              ]
#print(matrix)

#for element in matrix:
    #print(' '.join([str(a) for a in element]))

#rows = len(matrix)
#cols = len(matrix[0])
#for r in range(rows):
    #for c in range(r):
        #matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
    #for r in range(rows):
        #for c in range(cols // 2):
            #matrix[r][c], matrix[r][cols - c - 1] = matrix[r][cols - c - 1], matrix[r][c]
#for element in matrix:
    #print(' '.join([str(a) for a in element]))