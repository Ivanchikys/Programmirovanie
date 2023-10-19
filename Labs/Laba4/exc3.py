string =input('Введите строку с 2 и более h')              #Вводим слово и просим пользователя ввести минимально 2 h

first_h = string.find('h')               #Первое вхождение h
last_h = string.rfind('h')               #Второе вхождение h

result = string[:first_h ] + string[last_h  + 1:]  # строка от  0 до h) + от h] до конца

print(result)
