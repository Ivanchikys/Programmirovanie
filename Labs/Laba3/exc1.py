
a = int(input('Введите A: '))
b = int(input('Введите B: '))

move = 1 if a < b else -1

for i in range (a ,b + move, move):
    print(i)