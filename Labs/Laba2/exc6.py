x=int(input('Введите абсциссу x'))
y=int(input('Введите ординату y'))

if x>0 and y>0:
    print('I четверть')

elif x<0 and y>0:
    print('II четверть')

elif x<0 and y<0:
    print('III четверть')

else:
    print('IV четверть')
