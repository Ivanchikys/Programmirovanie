#Дан текст. 
#Выведите все слова, встречающиеся в тексте, по одному на каждую строку. 
#Слова должны быть отсортированы по убыванию их количества появления в тексте, 
#а при одинаковой частоте появления — в лексикографическом порядке

text =  '''
    hi
    hi
    what is your name
    my name is bond
    james bond
    my name is damme
    van damme
    claude van damme
    jean claude van damme
'''
words = text.split()  
freq = {}                      #сюда будем заносить частоты

for word in words:
    freq[word] = freq.get(word, 0) + 1     # кол-во частот слова. 1+1 если ворд встреча. 0+1 если оно одно.
#print (freq)

freqList = [ (count,word) for word, count in freq.items() ]
freqList.sort(key=lambda x: (-x[0], x[1]))

for count  , word in freqList:
    print(word)