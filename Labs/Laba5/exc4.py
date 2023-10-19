#Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
for element in a:
    if element not in c:
        a_element = a.count(element)
        b_element = b.count(element)
        min_count = min(a_element, b_element)
        for i in range(min_count):
            c.append(element)
print(c)