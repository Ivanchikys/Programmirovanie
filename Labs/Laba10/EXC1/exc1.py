#Во входном файле записаны 10 целых чисел, каждое в отдельной строке. 
#Считать из текстового файла числа и записать их в другой текстовый файл в отсортированном виде.

file =  open('Labs/Laba10/EXC1/exc1_input.txt', 'r') 
numbers = [int(line.strip()) for line in file]

numbers.sort()


file = open('Labs/Laba10/EXC1/exc1_output.txt', 'w')

for number in numbers:
    file.write(str(number) + '\n')

print(file)
file.close()
