#В списке, состоящем из положительных и отрицательных целых чисел,
#найти первый, третий и шестой положительные элементы и вычислить их произведение
numbers = [-1, 4, 5, 7, -5, -2, 6, 2, 8, -4]
numbers_positive = []
for number in numbers:
    if number > 0:
        numbers_positive.append(number)
print(numbers_positive)

composition = numbers_positive[0] * numbers_positive[2] * numbers_positive[5]
print(composition)


