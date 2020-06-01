import random

filepath = "lab3/otkrytii_tekst.txt"

with open(filepath , "r", encoding="utf-8") as file:
    open_text = file.read() #считали файл посимвольно
open_text = list(open_text)#сделали из считанной строки список (преобразовать к нормальному виду) 

print(open_text) #напечатали результат


bukvi_orig = [] # создаем список для алфавита
for i in open_text: # проверяем на наличие уникальных символов наш список
    if i not in bukvi_orig: # если в списке есть уникальный символ
        bukvi_orig.append(i) # добавляем его в список

#отсутствует запись алфавита в отдельный файл

print(bukvi_orig) # печатаем результат алфавита

bukvi_encrypt = bukvi_orig.copy() # создаем маску список для алфавита
random.shuffle(bukvi_encrypt) # мешаем буквы с алфавита


key_encrypt = {} # создаем словарь для шифрования
key_decrypt = {} # создаем словарь для дешифрования
for i in range(len(bukvi_orig)): # проходимся по алфавиту и 
    key_encrypt.update(dict([(bukvi_orig[i],bukvi_encrypt[i])])) # записываем рядом с настояще буквой ее зашифрованную
    key_decrypt.update(dict([(bukvi_encrypt[i],bukvi_orig[i])])) # записываем рядом с зашифрованной буквой ее настоящую

shifr_text = [] # создаем список для шифртекста
for i in open_text: # проходимся по буквам переменной в которой хранится шифртекст 
    temp_letter = key_encrypt[i] # временная буква в которой хранится зашифрованная буква соответствующая данной настоящей
    shifr_text.append(temp_letter) # добавляем в зашифрованный список эту букву

print(shifr_text) # печатаем зашифрованный текст

deshifr_text = [] # расшифровываем текст
for i in shifr_text: # проходимся по списку с зашифрованным текстом
    temp_letter = key_decrypt[i] # временная буква для перевода ширбуквы в нормальную согласно словарю
    deshifr_text.append(temp_letter) # добавление расшифрованной буквы в список расшифрованного текста


print(deshifr_text) # печатаем результат расшифровки
