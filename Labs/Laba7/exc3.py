import random

numbers1 = [random.randint(0,100000) for _ in range(100000)]
numbers2 = [random.randint(0,100000) for _ in range(100000)]

print(len(set(numbers1) & set(numbers2)))


