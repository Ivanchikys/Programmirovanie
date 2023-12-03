iterations = int(input("Введите N: "))

if iterations > 100: 
    print("Вы ввели N, превышающее 100, программа выполняться не будет.")
    
else: 
    s = 1

    for i in range(2, iterations + 1):
        s += 1/i

    print(f"S = {s}")