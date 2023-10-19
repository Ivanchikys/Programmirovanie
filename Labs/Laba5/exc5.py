#В списке найти количество элементов, значение которых не меньше заданного минимума и не больше заданного максимума,
#то есть принадлежат определенному диапазону. Пусть список заполняется случайными числами, границы диапазона задаются с клавиатуры.
import random

numbers = [random.randint(50, 100) for _ in range(18)]
print(numbers)

minimum = int(input('Минимальное значение: '))
maximum = int(input('Максимальное значение: '))

count = 0
for i in numbers:
    if minimum <= i <= maximum:
        count += 1

print(count)