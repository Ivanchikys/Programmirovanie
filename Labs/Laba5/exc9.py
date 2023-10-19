numbers = [int(i) for i in input().split()]

if numbers == numbers[::-1]:
    print('Симметрия есть')

else:
    print('Няма симметрии')
