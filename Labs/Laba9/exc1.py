def shift_left(lst, n):

    n = n % len(lst)
    lst = lst[n:] + lst[:n]

    return lst

lst = [1, 2, 3, 4, 5]
n = int(input('Введите шаг сдвига: '))

print("Исходный список:", lst)

lst_shifted_left = shift_left(lst, n)

print("Список после циклического сдвига влево на", n, "шагов:", lst_shifted_left)