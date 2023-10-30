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
errors = {
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
    messages = ''
     
    if not hashtags:    
        return []
    
    hashtags = hashtags.split()

    hashtags = [hashtag.lower() for hashtag in hashtags]

    for hashtag in hashtags:

        if not hashtag.startswith('#'):
            errors['startWith'] = True
       
        if hashtag == '#':
            errors['notOneSymbol'] = True
        
        if hashtag.find('#',1) != -1:
            errors['spaces'] = True
        
        if hashtags.count(hashtag) > 1: 
            errors['unique'] = True
        
        if len(hashtag) > 20:
            errors['tooLong']  = True

    if len(hashtags) > 5: 
        errors['tooMany'] = True

    for errorName in errors:
        if errors[errorName]:
            messages += '\n' + errorMessages[errorName]

    if len(messages)  != 0:
        return messages
    
    return ' '.join(hashtags)

hashtags =  '#yalta #grodno #python #Dzerzhinskogo #Paparaci papalepka #Jamajka #Jamajka  '            #input('Введите хеш-теги')  

print(validateHashtags(hashtags))
