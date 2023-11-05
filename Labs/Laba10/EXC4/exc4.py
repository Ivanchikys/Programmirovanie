#Написать программу, 
#которая считает количество строк, слов и букв в переданном ей файле.
file =  open('Labs/Laba10/EXC4/input.txt', 'r') 

lines = 0
words = 0 
letters = 0

for line in file:
    lines += 1 
    words += len(line.split() )
    for char in line:
        if char != ' ' and char != '.' and char != '\n': 
            letters += 1

print(lines)
print(letters)
print(words)

file = open('Labs/Laba10/EXC4/output.txt', 'w')

file.write('Lines: ' + str(lines) + '\n' )
file.write('Letters: '  + str(letters) + '\n' )
file.write('Words: ' + (str(words) ))

print(file)
file.close()