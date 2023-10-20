#Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение. Вторично дублировать выведенное значение не нужно.
from random import randint

table1 = [randint(1, 15)
       for i in range(15)]
table2 = []

for i in range(len(table1)):
    if table1.count(table1[i]) > 1 and table1[i] not in(table2):
        table2.append(table1[i])

print(table2)