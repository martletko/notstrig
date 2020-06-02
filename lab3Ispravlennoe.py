import random


class MyAbstractClass():
    def read_text(self, filepath):
        """читаем из файла текста который тхт и который надо зашифровать
           и сохраняем содержимое текста в список open_text"""
        open_text = ""
        with open(filepath , "r", encoding="utf-8") as file:
            line = file.readline()
            while line:
                line = line.replace('\n','')
                open_text += line
                line = file.readline()
        open_text = list(open_text)
        return open_text

class shifr_zamena(MyAbstractClass):
    """класс читает текст построчно, создает алфавит из уник символов текста,
       создает ключ, словаь дешифрования и шифрования, шифрует и расшифровывает текст"""

    def generate_alphabet_zamena(self, open_text):
        """функция создает список алфавита в который добавляет каждый уникальный 
           символ который есть в тексте"""
        bukvi_orig = [] # создаем список для алфавита
        for i in open_text: # проверяем на наличие уникальных символов наш список
            if i not in bukvi_orig: # если в списке есть уникальный символ
                bukvi_orig.append(i) # добавляем его в список
        return bukvi_orig 
    
    def generate_key_zamena(self, bukvi_orig):
        """функция которая создает маску списка алфавита и перемешивает буквы 
        создавая ключ"""
        bukvi_encrypt = bukvi_orig.copy() # создаем маску список для алфавита
        random.shuffle(bukvi_encrypt) # мешаем буквы с алфавита 
        return bukvi_encrypt
    
    def generate_key_decrypt_zamena(self, bukvi_orig, bukvi_encrypt):
        """функция которая создает словарь для дешифрования"""
        key_decrypt = {} # создаем словарь для дешифрования
        for i in range(len(bukvi_orig)):
            key_decrypt.update(dict([(bukvi_encrypt[i],bukvi_orig[i])])) # записываем рядом с зашифрованной буквой ее настоящую
        return key_decrypt

    def generate_key_encrypt_zamena(self,bukvi_orig, bukvi_encrypt):
        """функция которая создает словарь для ширования"""
        key_encrypt = {} # создаем словарь для шифрования
        for i in range(len(bukvi_orig)): # проходимся по алфавиту и 
            key_encrypt.update(dict([(bukvi_orig[i],bukvi_encrypt[i])])) # записываем рядом с настояще буквой ее зашифрованную
        return key_encrypt

    def generate_shifr_text_zamena(self, key_encrypt,open_text):
        """функция которая шифрует текст """
        shifr_text = [] # создаем список для шифртекста
        for i in open_text: # проходимся по буквам переменной в которой хранится шифртекст 
            temp_letter = key_encrypt[i] # временная буква в которой хранится зашифрованная буква соответствующая данной настоящей
            shifr_text.append(temp_letter) # добавляем в зашифрованный список эту букву
        return shifr_text

    def generate_deshifr_text_zamena(self,key_decrypt,shifr_text):
        """ функция которая расшифровывает текст"""
        deshifr_text = [] # расшифровываем текст
        for i in shifr_text: # проходимся по списку с зашифрованным текстом
            temp_letter = key_decrypt[i] # временная буква для перевода ширбуквы в нормальную согласно словарю
            deshifr_text.append(temp_letter) # добавление расшифрованной буквы в список расшифрованного текста
        return deshifr_text

class shifr_perestanovka(MyAbstractClass):
    def generate_key_perestanovka(self, key_len_perestanovka):
        """функция которая генерирует ключ для перестановки"""
        key_perestanovka = []
        for i in range(1,key_len_perestanovka + 1): 
            key_perestanovka.append(i)
        random.shuffle(key_perestanovka) 
        return key_perestanovka

    def add_space_perestanovka(self, open_text,key_len_perestanovka):
        """функция дополняет текст пробелами до длины кратной длине ключа """
        while len(open_text) % key_len_perestanovka != 0:
            open_text.append(' ')
        return open_text

    def generate_shifr_text_perestanovka(self, open_text, key_len_perestanovka,key_perestanovka):
        """функция генерации зашифрованного текста """
        shifr_text = []
        for i in range(0 ,len(open_text) , key_len_perestanovka):
            temp_list = open_text[i:i+key_len_perestanovka]
            temp_list_mask = temp_list.copy()
            for k in range(key_len_perestanovka):
                temp_num = int(key_perestanovka[k])
                temp_list_mask[k] = temp_list[temp_num - 1]
            shifr_text.extend(temp_list_mask)    
        return shifr_text
    
    def generate_deshifr_text_perestanovka(self, open_text, key_len_perestanovka,shifr_text,key_perestanovka):
        """функция расшифровки текста """
        deshifr_text = []
        for i in range(0 ,len(open_text) , key_len_perestanovka):
            temp_list = shifr_text[i:i+key_len_perestanovka]
            temp_list_mask = temp_list.copy()
            for k in range(key_len_perestanovka):
                temp_num = int(key_perestanovka[k])
                temp_list_mask[temp_num-1] = temp_list[k]
            deshifr_text.extend(temp_list_mask)
        return deshifr_text
    
class shifr_gammirovanie(MyAbstractClass):
    
    def generate_alphabet_gammirovanie(self, open_text):
        bukvi_orig_gamm = []
        for i in open_text:
            if i not in bukvi_orig_gamm:
                bukvi_orig_gamm.append(i)
        return bukvi_orig_gamm
    
    def generate_key_gamm(self,key_len_gamm,bukvi_orig_gamm):
        key_gamm = []
        while True:
            new_val = random.randint(0, len(bukvi_orig_gamm) - 1)
            if new_val not in key_gamm:
                key_gamm.append(new_val)
            if len(key_gamm) == key_len_gamm:
                break
        return key_gamm
    
    def add_space_gammirovanie(self,open_text,key_len_gamm):
        while len(open_text) % key_len_gamm != 0:
            open_text.append(' ')
        return open_text

    def generate_shifr_text_gammirovanie(self,open_text,key_len_gamm,bukvi_orig_gamm,key_gamm):
        shifr_text_gamm = []
        for i in range(0 ,len(open_text) , key_len_gamm):
            temp_list = open_text[i:i+key_len_gamm]
            for k in range(key_len_gamm):
                new_index = (bukvi_orig_gamm.index(temp_list[k]) + int(key_gamm[k])) % len(bukvi_orig_gamm)
                temp_list[k] = bukvi_orig_gamm[new_index]
            shifr_text_gamm.extend(temp_list)
        return shifr_text_gamm
        
    def generate_deshifr_text_gammirovanie(self,open_text,key_len_gamm,bukvi_orig_gamm,key_gamm,shifr_text_gamm):
        deshifr_text_gamm = []
        for i in range(0 ,len(open_text) , key_len_gamm):
            temp_list = shifr_text_gamm[i:i+key_len_gamm]
            for k in range(key_len_gamm):
                new_index = (bukvi_orig_gamm.index(temp_list[k]) - int(key_gamm[k])) % len(bukvi_orig_gamm)
                temp_list[k] = bukvi_orig_gamm[new_index]
            deshifr_text_gamm.extend(temp_list)
        return deshifr_text_gamm

main_flag = True
while main_flag:
    print(".>> Главное меню") #
    print(".>> 	1) Зашифровать/Расшифровать") #
    print(".>> 	2) Сгенерировать ключ") #
    
    num1 = input("введите номер:... ")
    if num1.isnumeric() == True:
        pass
    else:
        print("введите целое число  ")
        continue
    num1 = int(num1)
    if num1 != 1 and num1 != 2:
        print("число должно быть или 1 или 2")
        continue
    else:
        pass
    if num1 == 1: # Зашифровать/Расшифровать
        print(".>> Зашифровать/Расшифровать")
        print(".>> 	1) Зашифровать")
        print(".>>  2) Расшифровать")
        num1_1 = input("введите номер: ... ")
        
    
                
        if num1_1.isnumeric() == True:
            pass
        else:
            print("введите целое число")
        num1_1 = int(num1_1)
        if num1_1 !=1 and num1_1 !=2 :
            print("число должно быть 1 или 2")
            continue
        else:
            pass

        if num1_1 == 1: #зашифровать/расшифровать -> зашифровать
            print(".>> выберите метода шифровки")
            print(".>> 1) замена")
            print(".>> 2) перестановка")
            print(".>> 3) гамирование")
            num_of_shifr = (input("выберите метод шифрования:..."))   
            if num_of_shifr.isnumeric() == True:
                pass
            else:
                print("введите целое число")
                continue
            num_of_shifr = int(num_of_shifr)
            if num_of_shifr != 1 and num_of_shifr != 2 and num_of_shifr != 3:
                print("число должно быть 1,  2 или 3")
                continue
            else:
                pass        

            if num_of_shifr == 1: #замена
                filepath = input("etner path to txt.txt ... ")

                filepath_check = filepath.split(".")
                if filepath_check[-1] != "txt":
                    print("файл должен быть формата txt ")
                    continue
                else:
                    pass

                keypath = input("enter path to key")

                keypath_check = keypath.split(".")
                if keypath_check[-1] != "key":
                    print("файл должен быть формата key")
                    continue
                else:
                    pass

                bukvi_orig = []
                bukvi_encrypt = []
                with open(keypath, "r", encoding="utf-8" ) as key:
                    check_phrase_shifr_zamena = "key_zamena\n"
                    first_line = key.readline()
                    if first_line != check_phrase_shifr_zamena:
                        print('wrong key')
                        continue
                    else:
                        pass
                    for temp_line in key:
                        bukvi_orig.append(temp_line[0])
                        bukvi_encrypt.append(temp_line[2])    

                encryptpath = input("введите название для файла в котором хранится зашифрованный текст, файл должен быть формата encrypt... ")
                

                encryptpath_check = encryptpath.split(".")
                if encryptpath_check[-1] != "encrypt":
                    print("файл должен быть формата encrypt")
                    continue
                else:
                    pass

                
                obj1 = shifr_zamena()
                open_text = obj1.read_text(filepath)
                key_encrypt = obj1.generate_key_encrypt_zamena(bukvi_orig,bukvi_encrypt)
                shifr_text_zamena = obj1.generate_shifr_text_zamena(key_encrypt,open_text)   
                with open(encryptpath, "w", encoding="utf-8" ) as shifrtext:
                    check_phrase_shifr_zamena = "key_zamena\n"
                    shifrtext.write(check_phrase_shifr_zamena)
                    for i in range(len(shifr_text_zamena)):
                        shifrtext.write(shifr_text_zamena[i])
                print('текст зашифрован')

            elif num_of_shifr == 2:# перестановка
                filepath = input("etner path to txt.txt ... ")

                filepath_check = filepath.split(".")
                if filepath_check[-1] != "txt":
                    print("файл должен быть формата txt ")
                    continue
                else:
                    pass

                keypath = input("enter path to key")

                keypath_check = keypath.split(".")
                if keypath_check[-1] != "key":
                    print("файл должен быть формата key")
                    continue
                else:
                    pass
                    
                key_perestanovka = []
                with open(keypath, "r", encoding="utf-8" ) as key:
                    check_phrase_shifr_perestanovka = "key_perestanovka\n"
                    first_line = key.readline()
                    if first_line != check_phrase_shifr_perestanovka:
                        print('wrong key')
                        break
                    else:
                        print('проверка на ключ шифра: успешно')   
                    for temp_line in key:
                        temp_line.rstrip('\n')
                        key_perestanovka.append(temp_line)

                encryptpath = input("введите название для файла в котором хранится зашифрованный текст, файл должен быть формата encrypt... ")
                

                encryptpath_check = encryptpath.split(".")
                if encryptpath_check[-1] != "encrypt":
                    print("файл должен быть формата encrypt")
                    continue
                else:
                    pass
                
                obj2 = shifr_perestanovka()
                open_text = obj2.read_text(filepath)
                key_len_perestanovka = len(key_perestanovka)
                open_text = obj2.add_space_perestanovka(open_text,key_len_perestanovka)
                shifr_text_perestanovka = obj2.generate_shifr_text_perestanovka(open_text,key_len_perestanovka,key_perestanovka)
                with open(encryptpath, "w", encoding="utf-8" ) as shifrtext:
                    check_phrase_shifr_perestanovka = "key_perestanovka\n"
                    shifrtext.write(check_phrase_shifr_perestanovka)
                    for i in range(len(shifr_text_perestanovka)):
                        shifrtext.write(shifr_text_perestanovka[i])
                print('текст зашифрован')
            
            elif num_of_shifr == 3: #гаммирование

                filepath = input("etner path to txt.txt ... ")

                filepath_check = filepath.split(".")
                if filepath_check[-1] != "txt":
                    print("файл должен быть формата txt ")
                    continue
                else:
                    pass

                keypath = input("enter path to key")

                keypath_check = keypath.split(".")
                if keypath_check[-1] != "key":
                    print("файл должен быть формата key")
                    continue
                else:
                    pass

                key_gamm = []
                with open(keypath, "r", encoding="utf-8" ) as key:
                    check_phrase_shifr_gammirovanie = "key_gammirovanie\n"
                    first_line = key.readline()
                    if first_line != check_phrase_shifr_gammirovanie:
                        print('wrong key')
                        break
                    else:
                        print('проверка на ключ шифра: успешно') 
                    for temp_line in key:
                        temp_line = temp_line.split(' ')
                        temp_line.pop()
                        key_gamm.extend(temp_line)
                
                encryptpath = input("введите название для файла в котором хранится зашифрованный текст, файл должен быть формата encrypt... ")
                

                encryptpath_check = encryptpath.split(".")
                if encryptpath_check[-1] != "encrypt":
                    print("файл должен быть формата encrypt")
                    continue
                else:
                    pass

                key_len_gamm = len(key_gamm)
                obj3 = shifr_gammirovanie()
                open_text = obj3.read_text(filepath)
                bukvi_orig_gamm = obj3.generate_alphabet_gammirovanie(open_text)
                open_text = obj3.add_space_gammirovanie(open_text,key_len_gamm)
                shifr_text_gamm = obj3.generate_shifr_text_gammirovanie(open_text,key_len_gamm,bukvi_orig_gamm,key_gamm)
                with open(encryptpath, "w", encoding="utf-8" ) as shifrtext:
                    check_phrase_shifr_gammirovanie = "key_gammirovanie\n"
                    shifrtext.write(check_phrase_shifr_gammirovanie)
                    for i in range(len(shifr_text_gamm)):
                        shifrtext.write(shifr_text_gamm[i])
                print('текст зашифрован')                

        elif num1_1 == 2: #зашифровать/расшифровать -> расшифровать
            print(".>> выберите метода дешифровки")
            print(".>> 1) замена")
            print(".>> 2) перестановка")
            print(".>> 3) гамирование")

            num_of_deshifr = input("выберите метод шифрования:...") 
            if num_of_deshifr.isnumeric() == True:
                pass
            else:
                print("введите целое число")
                continue
            num_of_deshifr = int(num_of_deshifr)
            if num_of_deshifr != 1 and num_of_deshifr != 2 and num_of_deshifr != 3:
                print("число должно быть 1,  2 или 3")
                continue
            else:
                pass        

            if num_of_deshifr == 1: #расшифровать замена

                filepath = input("etner path to txt.txt ... ")

                filepath_check = filepath.split(".")
                if filepath_check[-1] != "txt":
                    print("файл должен быть формата txt ")
                    continue
                else:
                    pass

                keypath = input("enter path to key")

                keypath_check = keypath.split(".")
                if keypath_check[-1] != "key":
                    print("файл должен быть формата key")
                    continue
                else:
                    pass                

                bukvi_orig = []
                bukvi_encrypt = []
                
                with open(keypath,"r",encoding="utf-8") as key:
                    check_phrase_shifr_zamena = "key_zamena\n"
                    first_line = key.readline()
                    if first_line != check_phrase_shifr_zamena:
                        print("wrong_key")
                        break
                    else:
                        print("проверка на ключ шифра: успешно")
                    for temp_line in key:
                        
                        bukvi_orig.append(temp_line[0])
                        bukvi_encrypt.append(temp_line[2])  #считали ключ 

                encryptpath = input("введите название для файла в котором хранится зашифрованный текст, файл должен быть формата encrypt... ")
                

                encryptpath_check = encryptpath.split(".")
                if encryptpath_check[-1] != "encrypt":
                    print("файл должен быть формата encrypt")
                    continue
                else:
                    pass

                shifr_text_zamena = []
                
                with open(encryptpath, "r", encoding="utf-8" ) as shifrtext:
                    check_phrase_shifr_zamena = "key_zamena\n"
                    first_line = shifrtext.readline()
                    if first_line != check_phrase_shifr_zamena:
                        print('wrong key')
                        break
                    else:
                        print('проверка на ключ шифра: успешно')
                    line = shifrtext.readline(-1)
                    line = list(line)                    
                    shifr_text_zamena.extend(line) #считали шифр

                decryptpath = input("введите название для файла в котором хранится расшифрованный текст, файл должен быть формата txt... ")
                

                decryptpath_check = decryptpath.split(".")
                if decryptpath_check[-1] != "txt":
                    print("файл должен быть формата txt")
                    continue
                else:
                    pass
                
                obj1 = shifr_zamena()
                open_text = obj1.read_text(filepath)
                key_decrypt = obj1.generate_key_decrypt_zamena(bukvi_orig,bukvi_encrypt)
                deshifr_text_zamena = obj1.generate_deshifr_text_zamena(key_decrypt,shifr_text_zamena) #расшифровали

                with open(decryptpath, "w", encoding="utf-8" ) as decryptedtext:
                    for i in range(len(deshifr_text_zamena)):
                        decryptedtext.write(deshifr_text_zamena[i])
                print('текст расшифрован')

            elif num_of_deshifr == 2: #расшифровать перестановка
                filepath = input("etner path to txt.txt ... ")

                filepath_check = filepath.split(".")
                if filepath_check[-1] != "txt":
                    print("файл должен быть формата txt ")
                    continue
                else:
                    pass

                keypath = input("enter path to key")

                keypath_check = keypath.split(".")
                if keypath_check[-1] != "key":
                    print("файл должен быть формата key")
                    continue
                else:
                    pass                               

                key_perestanovka = []

                with open(keypath,"r",encoding="utf-8") as key:
                    check_phrase_shifr_perestanovka = "key_perestanovka\n"
                    first_line = key.readline()
                    if first_line != check_phrase_shifr_perestanovka:
                        print("wrong_key")
                        break
                    else:
                        print("проверка на ключ шифра: успешно")
                    for temp_line in key:
                        temp_line = temp_line.replace('\n','')
                        key_perestanovka.append(temp_line)
                
                encryptpath = input("введите название для файла в котором хранится зашифрованный текст, файл должен быть формата encrypt... ")
                

                encryptpath_check = encryptpath.split(".")
                if encryptpath_check[-1] != "encrypt":
                    print("файл должен быть формата encrypt")
                    continue
                else:
                    pass

                shifr_text_perestanovka = []

                with open(encryptpath, "r", encoding="utf-8" ) as shifrtext:
                    check_phrase_shifr_perestanovka = "key_perestanovka\n"
                    first_line = shifrtext.readline()
                    if first_line != check_phrase_shifr_perestanovka:
                        print('wrong key')
                        break
                    else:
                        print('проверка на ключ шифра: успешно')
                    line = shifrtext.readline(-1)
                    line = list(line)                    
                    shifr_text_perestanovka.extend(line) #считали шифр 

                
                decryptpath = input("введите название для файла в котором хранится расшифрованный текст, файл должен быть формата txt... ")
                

                decryptpath_check = decryptpath.split(".")
                if decryptpath_check[-1] != "txt":
                    print("файл должен быть формата txt")
                    continue
                else:
                    pass

                key_len_perestanovka = len(key_perestanovka)
                obj2 = shifr_perestanovka()
                open_text = obj2.read_text(filepath)
                deshifr_text_perestanovka = obj2.generate_deshifr_text_perestanovka(open_text,key_len_perestanovka,shifr_text_perestanovka,key_perestanovka)

                print(" расшифрованно успешно смотрите результаты в файле с названием " + decryptpath)

            elif num_of_deshifr == 3: #расшифровать гаммирование
                filepath = input("etner path to txt.txt ... ")

                filepath_check = filepath.split(".")
                if filepath_check[-1] != "txt":
                    print("файл должен быть формата txt ")
                    continue
                else:
                    pass

                keypath = input("enter path to key")

                keypath_check = keypath.split(".")
                if keypath_check[-1] != "key":
                    print("файл должен быть формата key")
                    continue
                else:
                    pass           

                key_gamm = []

                with open(keypath,"r",encoding="utf-8") as key:
                    check_phrase_shifr_gammirovanie = "key_gammirovanie\n"
                    first_line = key.readline()
                    if first_line != check_phrase_shifr_gammirovanie:
                        print("wrong_key")
                        break
                    else:
                        print("проверка на ключ шифра: успешно")
                    for temp_line in key:
                        temp_line = temp_line.replace('\n','')
                        temp_line.rstrip(' ')
                        temp_line = temp_line.split(' ')
                        key_gamm.extend(temp_line)

                encryptpath = input("введите название для файла в котором хранится зашифрованный текст, файл должен быть формата encrypt... ")
                

                encryptpath_check = encryptpath.split(".")
                if encryptpath_check[-1] != "encrypt":
                    print("файл должен быть формата encrypt")
                    continue
                else:
                    pass

                shifr_text_gamm = []

                with open(encryptpath, "r", encoding="utf-8" ) as shifrtext:
                    check_phrase_shifr_gammirovanie = "key_gammirovanie\n"
                    first_line = shifrtext.readline()
                    if first_line != check_phrase_shifr_gammirovanie:
                        print('wrong key')
                        break
                    else:
                        print('проверка на ключ шифра: успешно')
                    line = shifrtext.readline(-1)
                    line = list(line)                    
                    shifr_text_gamm.extend(line) #считали шифр 

                decryptpath = input("введите название для файла в котором хранится расшифрованный текст, файл должен быть формата txt... ")
                

                decryptpath_check = decryptpath.split(".")
                if decryptpath_check[-1] != "txt":
                    print("файл должен быть формата txt")
                    continue
                else:
                    pass

                obj3 = shifr_gammirovanie()
                open_text = obj3.read_text(filepath)
                deshifr_text_gamm = obj3.generate_deshifr_text_gammirovanie(open_text,key_len_gamm,bukvi_orig_gamm,key_gamm,shifr_text_gamm)
               
                with open(decryptpath, "w", encoding="utf-8" ) as decryptedtext:
                    for i in range(len(deshifr_text_gamm)):
                        decryptedtext.write(deshifr_text_gamm[i])
                print('текст расшифрован')

    elif num1 == 2: # сгенерировать ключ
        print(".>> Сгенерировать ключ для следующего алгоритма: ")
        print(".>> 1) шифр замены")
        print(".>> 2) шифр перестановки")
        print(".>> 3) шифр гаммирования")
        num_of_shifr = (input("выберите метод шифрования:..."))   
        if num_of_shifr.isnumeric() == True:
            pass
        else:
            print("введите целое число")
            continue
        num_of_shifr = int(num_of_shifr)
        if num_of_shifr != 1 and num_of_shifr != 2 and num_of_shifr != 3:
            print("число должно быть 1,  2 или 3")
            continue
        else:
            pass        

        if num_of_shifr == 1:
            filepath = input("etner path to txt.txt ... ")

            filepath_check = filepath.split(".")
            if filepath_check[-1] != "txt":
                print("файл должен быть формата txt ")
                continue
            else:
                pass

            obj1 = shifr_zamena()
            open_text = obj1.read_text(filepath)
            bukvi_orig = obj1.generate_alphabet_zamena(open_text)
            bukvi_encrypt = obj1.generate_key_zamena(bukvi_orig)
            key_decrypt = obj1.generate_key_decrypt_zamena(bukvi_orig,bukvi_encrypt)
            key_encrypt = obj1.generate_key_encrypt_zamena(bukvi_orig,bukvi_encrypt)
            
            keypath = input("enter path to key")

            keypath_check = keypath.split(".")
            if keypath_check[-1] != "key":
                print("файл должен быть формата key")
                continue
            else:
                pass

            with open(keypath, "w", encoding="utf-8" ) as key:
                check_phrase_shifr_zamena = "key_zamena\n"
                key.write(check_phrase_shifr_zamena)
                for key1 in key_encrypt:
                    line = key1 + ' ' + key_encrypt[key1] + '\n'
                    key.write(line) 
            
            print("the key has been succesfully saved ...")    

        elif num_of_shifr == 2: # шифр перестановка   
            filepath = input("etner path to txt.txt ... ")

            filepath_check = filepath.split(".")
            if filepath_check[-1] != "txt":
                print("файл должен быть формата txt ")
                continue
            else:
                pass 

            key_len_perestanovka = (input("enter key length... (int number) "))
            if key_len_perestanovka.isnumeric() == True:
                pass
            else:
                print("введите целое число  ")
                continue
            key_len_perestanovka = int(key_len_perestanovka)
            if key_len_perestanovka < 0:
                print("число должно быть больше 0")
                continue
            else:
                pass

            
            obj2 = shifr_perestanovka()
            open_text = obj2.read_text(filepath)
            key_perestanovka = obj2.generate_key_perestanovka(key_len_perestanovka)

            key_name = input("enter path to key")

            keypath_check = keypath.split(".")
            if keypath_check[-1] != "key":
                print("файл должен быть формата key")
                continue
            else:
                pass

            with open(key_name, "w", encoding="utf-8" ) as key:
                check_phrase_shifr_perestanovka = "key_perestanovka\n"
                key.write(check_phrase_shifr_perestanovka)
                for i in range(len(key_perestanovka)):
                    tmp_l = str(key_perestanovka[i]) + '\n'
                    key.write(tmp_l) 
        
            print("the key has been succesfully saved ...")


        elif num_of_shifr == 3: # шифр гамирование
            filepath = input("etner path to txt.txt ... ")

            filepath_check = filepath.split(".")
            if filepath_check[-1] != "txt":
                print("файл должен быть формата txt ")
                continue
            else:
                pass     

            key_len_gamm = (input("enter key length... (int number) "))
            if key_len_gamm.isnumeric() == True:
                pass
            else:
                print("введите целое число  ")
                continue
            key_len_gamm = int(key_len_gamm)
            if key_len_gamm < 0:
                print("число должно быть больше 0")
                continue
            else:
                pass     

            obj3 = shifr_gammirovanie()
            open_text = obj3.read_text(filepath)
            bukvi_orig_gamm = obj3.generate_alphabet_gammirovanie(open_text)
            key_gamm = obj3.generate_key_gamm(key_len_gamm,bukvi_orig_gamm)
            
            key_name = input("enter path to key")

            keypath_check = keypath.split(".")
            if keypath_check[-1] != "key":
                print("файл должен быть формата key")
                continue
            else:
                pass

            with open(key_name, "w", encoding="utf-8" ) as key:
                check_phrase_shifr_gammirovanie = "key_gammirovanie\n"
                key.write(check_phrase_shifr_gammirovanie)
                for i in range(len(key_gamm)):
                    tmp_l = str(key_gamm[i]) + ' '
                    key.write(tmp_l) 
        
            print("the key has been succesfully saved ...")


