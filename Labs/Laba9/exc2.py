arr_in = [12, 23, 34, 45]
arr_out = []

for n in arr_in:
    sum_Digits = 0  

    for digit in str(n):
        sum_Digits += int(digit)
    arr_out.append(sum_Digits) 

print(arr_out)