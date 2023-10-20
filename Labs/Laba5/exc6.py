#В списке, состоящем из положительных и отрицательных целых чисел,
#найти первый, третий и шестой положительные элементы и вычислить их произведение
from random import randint

a = [randint(-5, 5)
    for i in range (20)]

multipl = 1
count = 0 
print(a)

for i in range(len(a)):
    if a[i] > 0:
        count += 1
        if count in (1, 3, 6):
            multipl *= a[i]

print(multipl)