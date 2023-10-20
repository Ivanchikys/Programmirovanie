numbers = '1 2 4 5 2 3 5 4'
snumber = set()

for number in numbers.split():
    if number in snumber:
        print('Yes')
    else:
        print('No')

    snumber.add(number)