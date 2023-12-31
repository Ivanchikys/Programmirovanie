#Дан текст (строк может быть много).
#Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
text = '''
    ваша лала стала лолай бубка
    лала азейрбаджан стала ваша бубка
    бубка лала
 '''  

words = text.split()  
freq = {}                      #сюда будем заносить частоты

for word in words:
    freq[word] = freq.get(word, 0) + 1     # кол-во частот слова. 1+1 если ворд встреча. 0+1 если оно одно.
#print (freq)

max_freq = max(freq.values())           #находит большее значение частот

for word, fr in freq.items():
    if fr == max_freq:
        result = (word,fr)      # найдём слово с наиб.част, которое 1-ое в лекс.порядке

print(result)