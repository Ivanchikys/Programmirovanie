#Считать из файла input.txt 10 чисел (числа записаны через пробел). 
#Затем записать их произведение в файл output.txt.

file =  open('Labs/Laba10/EXC3/input.txt', 'r') 
numbers = list(map(int, file.read().split() ))
Product = 1  

for number in numbers:
    Product *= number  

file = open('Labs/Laba10/EXC3/output.txt', 'w')

file.write(str(Product) )

print(file)
file.close()