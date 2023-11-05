#В файл записаны сведения о сотрудниках некоторой фирмы в виде:
# [Иванов 45 бухгалтер]
#Необходимо записать в текстовый файл сведения о сотрудниках, возраст которых меньше 40.

file =  open('Labs/Laba10/EXC5/input.txt', 'r')

Intelligence = [line for line in file if int(line.split()[1]) < 40 ]

print(Intelligence)

file = open('Labs/Laba10/EXC5/output.txt', 'w')
file.writelines(Intelligence)

print(file)
file.close()