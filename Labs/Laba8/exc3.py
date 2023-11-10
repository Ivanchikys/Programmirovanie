#Дана строка, содержащая хэш-теги. Необходимо провести валидацию правильности ввода хэш-тегов в соответствии с требованиями:

#● хэш-теги необязательны; F
#● хэш-тег начинается с символа # (решётка); T 
#● хеш-тег не может состоять только из одной решётки; T 
#● хэш-теги разделяются пробелами; T
#● один и тот же хэш-тег не может быть использован дважды; T
#● нельзя указать больше пяти хэш-тегов; T  
#● максимальная длина одного хэш-тега 20 символов, включая решётку; T
#● теги нечувствительны к регистру: #ХэшТег и #хэштег считаются одним и тем же тегом. F 

#Если валидация не соответствует требованиям, необходимо сформировать и вывести на экран строку, содержащую перечень ошибок
error = {
    'startWith': False,
    'notOneSymbol': False,
    'spaces': False,
    'unique': False,
    'tooLong': False,
    'tooMany': False,
}

errorMessages = {
    'startWith': 'Хэш-тег должен начинаться с решетки (#)',
    'notOneSymbol': 'Хэш-тег не может состоять только из решетки (#)',
    'spaces': 'Хэш-теги должны разделяться пробелами',
    'unique': 'Хэш-теги должен быть уникальным',
    'tooLong': 'Максимальная длина хэш-тега - 20 символов',
    'tooMany': 'Нельзя указать больше 5 хэш-тегов',
}

def validateHashtags(hashtags):
     
    if not hashtags:    
        return []
    
    hashtags = hashtags.split()

    hashtags = [hashtag.lower() for hashtag in hashtags]

    for hashtag in hashtags:
        error['startWith'] = not hashtag.startswith('#') or error['startWith']
        error['notOneSymbol'] = hashtag == '#' or error['notOneSymbol']
        error['spaces'] = hashtag.find('#',1) != -1 or  error['spaces']
        error['unique'] = hashtags.count(hashtag) > 1 or  error['unique']
        error['tooLong'] = len(hashtag) > 20 or error['tooLong']
    error['tooMany'] = len(hashtags) > 5 or  error['tooMany']

def printMessage (text):
    messages = ''

    validateHashtags(text)

    for errorName in error:
        if error[errorName]:
            messages += '\n' + errorMessages[errorName]

    if len(messages)  != 0:
        return messages
    
    return ' '.join(text)

hashtags = input('Введите хеш-теги ')                   #hashtags =  '#yalta #grodno #python #Dzerzhinskogo #Paparaci papalepka #Jamajka #Jamajka  '            

print(printMessage(hashtags))
