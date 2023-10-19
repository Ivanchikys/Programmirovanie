#Найти среднее арифметическое отрицательных элементов. Заменить на него минимальный элемент
numbers = [-1,2,3,7,-4,5,7,1,9]
negative_numbers = []

for number in numbers:
    if number < 0:                                #Добавление отриц.эл
        negative_numbers.append(number)

arithmetic_mean = sum(negative_numbers) / len(negative_numbers)         #Среднее арифметическое

min_index = numbers.index(min(numbers))
numbers[min_index] = arithmetic_mean

print(numbers)