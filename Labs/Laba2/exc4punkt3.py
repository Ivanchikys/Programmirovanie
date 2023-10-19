import math
x=int(input('Введите число X'))
if x>0 and x>8:
    y=40*3.14 + x
elif x==0:
    y=2 * math.tan(x) + x
elif x<0:
    y=math.sin(x) +  9*math.cos(x)
else:
    y=0
print(y)
