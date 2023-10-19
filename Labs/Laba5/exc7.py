#Поменять местами максимальный и минимальный элементы списка.
numbers = [1, 2, 4, 5, 6, 7, 8, 9]

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index] ,numbers[min_index]

print (numbers)