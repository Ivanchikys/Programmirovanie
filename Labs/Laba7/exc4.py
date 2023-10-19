import random

numbers1 = [random.randint(0,10000) for _ in range(10000)]
numbers2 = [random.randint(0,10000) for _ in range(10000)]
print(sorted (set(numbers1) & set(numbers2)))
