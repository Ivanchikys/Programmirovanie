number = input("Введите целое число: ")

even = 0
odd = 0

for digit in number:
    if int(digit) % 2 == 0:
        even += 1
    else: 
        odd += 1

print(f"Количество четных: {even}.\nКоличество нечетных: {odd}.")