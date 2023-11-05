#В файле записаны в строку через пробел целые числа. 
#Найти максимальное и минимальное число и записать в другой файл.
file =  open('Labs/Laba10/EXC2/exc2_input.txt', 'r') 
numbers = list(map(int, file.read().split() ))

print(numbers)

file = open('Labs/Laba10/EXC2/exc2_output.txt', 'w')

file.write(str (min(numbers)) + ' ')
file.write(str (max(numbers)) )


print(file)
file.close()
