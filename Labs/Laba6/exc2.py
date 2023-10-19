n = 4
a = [[2] * i + [1]  + [0] * (n - i - 1) for i in range(n)]
print(a)

for line in a:
    print(' '.join([str(element) for element in line]))
