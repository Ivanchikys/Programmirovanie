number = input("Введите натуральное число больше 0: ")

sum = 0
product = 1

for digit in number:
    sum += int(digit)

    if int(digit) != 0:
        product *= int(digit)

print(f"Сумма: {sum}.\nПроизведение: {product}.")