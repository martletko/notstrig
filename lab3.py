import random
import os

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
        tmp = len(bukvi_orig_gamm)
        for i in range(tmp):
            key_gamm.append(i)
        random.shuffle(key_gamm)
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

def pr_num1_2(num):
    if num.isnumeric() == True:
        num = int(num)
        if num == 1 or num == 2 or num == 3: 
            return True
        if num != 1 and num != 2 and num != 3:
            print("число должно быть или 1 или 2 or 3")
        return False
    else:
        print("введите целое число  ")
        return False
    
def pr_num1_3(num):
    if num.isnumeric() == True:
        num = int(num)
        if num == 1 or num == 2 or num == 3 or num == 4: 
            return True
        if num != 1 and num != 2 and num != 3 and num != 4:
            print("число должно быть или 1 или 2 или 3 или 4")
        return False
    else:
        print("введите целое число  ")
        return False

def check_symbols(input_text):
    error_symbols = ["\\","/",":", "*","?","\"","|", "<",">"]
    for i in input_text:
        if error_symbols.count(i) != 0:
            print("неверный символ в названии проверьте  чтобы таких символов не было /  : * ? | < >  ")
            return False
        else:
            return True

def check_format_txt(input_text):
    filepath_check = input_text.split(".")
    if filepath_check[-1] != "txt":
        print("файл должен быть формата txt ")
        return False
    else:
        return True

def check_format_key(input_text):
    keypath_check = input_text.split(".")
    if keypath_check[-1] != "key":
        print("файл должен быть формата key")
        return False
    else:
        return True

def check_format_encrypt(input_text):
    encryptpath_check = input_text.split(".")
    if encryptpath_check[-1] != "encrypt":
        print("файл должен быть формата encrypt")
        return False
    else:
        return True

def check_name(input_text):
    if input_text == ".encrypt":
        print("нельзя оставлять файл без названия")
        return False
    elif input_text == ".txt":
        print("нельзя оставлять файл без названия")
        return False
    elif input_text == ".key":
        print("нельзя оставлять файл без названия")
        return False
    else:
        return True

def check_errors_filepath(filepath, n):
    check_flag = check_format_txt(filepath)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")
        return 1
    else: 
        return 0

def check_errors_key_name_read(key_name, n):
    check_flag = check_format_key(key_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")   
        return 1
    check_flag = check_symbols(key_name)
    check_flag = check_name(key_name)
    if check_flag == False:
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")
        n += 1
        return 1
    return 0

def check_errors_key_name_write(key_name, n):
    check_flag = check_format_key(key_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")   
        return 1
    check_flag = check_symbols(key_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")
        return 1
    check_flag = check_name(key_name)
    if check_flag == False:
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")
        n += 1
        return 1
    return 0

def check_errors_encrypt_name_write(encrypt_name, n):
    check_flag = check_name(encrypt_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")   
        return 1
    check_flag = check_symbols(encrypt_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")   
        return 1
    check_flag = check_format_encrypt(encrypt_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")  
        return 1
    return 0

def check_errors_encrypt_name_read(encrypt_name, n):
    check_flag = check_name(encrypt_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")   
        return 1
    check_flag = check_format_encrypt(encrypt_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")  
        return 1
    return 0

def check_errors_decrypt_name_write(decrypt_name, n):
    check_flag = check_name(decrypt_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")   
        return 1
    check_flag = check_symbols(decrypt_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")   
        return 1
    check_flag = check_format_txt(decrypt_name)
    if check_flag == False:
        n += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - n),"попыток")  
        return 1
    return 0

folderpath = os.getcwd()
x = 0
while x < 3:
    #main menu
    print(".>> Главное меню") 
    print(".>> 	1) Зашифровать/Расшифровать") #
    print(".>> 	2) Сгенерировать ключ")
    print(".>>  3) выход") #
    num1 = input("введите номер:... ")

    check_flag = pr_num1_2(num1)
    if check_flag == False:
        x += 1
        print("неверный ввод, до выхода из программы осталось ", (3 - x),"попыток" )
    else:
        num1 = int(num1)

        y = 0
        while y < 3:
            if num1 == 1: # Зашифровать/Расшифровать
                print(".>> Зашифровать/Расшифровать")
                print(".>> 	1) Зашифровать")
                print(".>>\t2) Расшифровать")
                print(".>>\t3) выход")
                num1_1 = input("введите номер: ... ")
                check_flag = pr_num1_2(num1_1)
                if check_flag == False:
                    y += 1
                    print("неверный ввод, до выхода из программы осталось ", (3 - y),"попыток")
                else:
                    num1_1 = int(num1_1)
                    
                    z = 0
                    while z < 3:    
                        if num1_1 == 1: #зашифровать/расшифровать -> зашифровать
                            print(".>> выберите метода шифровки")
                            print(".>> 1) замена")
                            print(".>> 2) перестановка")
                            print(".>> 3) гамирование")
                            print(".>> 4) выход")
                            num_of_shifr = (input("выберите метод шифрования:..."))
                            check_flag = pr_num1_3(num_of_shifr)
                            if check_flag == False:
                                z += 1
                                print("неверный ввод, до выхода из программы осталось ", (3 - z),"попыток")
                            else:
                                num_of_shifr = int(num_of_shifr)
                                if num_of_shifr == 1: #замена
                                    z1 = 0
                                    while z1 < 3:
                                        z1_1 = z1
                                        filepath =  input("введите путь к тексту   ")

                                        z1_1 += check_errors_filepath(filepath, z1)
                                        if z1_1 > z1:
                                            z1 = z1_1
                                            continue

                                        key_name = input("введите имя ключа шифрования .key  ")

                                        z1_1 += check_errors_key_name_read(key_name, z1)
                                        if z1_1 > z1:
                                            z1 = z1_1
                                            continue
                                        
                                        keypath = os.path.join(folderpath, key_name)

                                        bukvi_orig = []
                                        bukvi_encrypt = []
                                        try:
                                            with open(keypath, "r", encoding="utf-8" ) as key:
                                                check_phrase_shifr_zamena = "key_zamena\n"
                                                first_line = key.readline()
                                                if first_line != check_phrase_shifr_zamena:
                                                    z1 += 1
                                                    print('неверный ключ, повторрите ввод ключа у вас осталось ', (3 - z1), "попыток")
                                                for temp_line in key:
                                                    bukvi_orig.append(temp_line[0])
                                                    bukvi_encrypt.append(temp_line[2])  
                                        except FileNotFoundError:
                                            print("нет файла, введите путь заново")
                                            z1 += 1
                                            print("неверный ввод, до выхода из программы осталось ", (3 - z1),"попыток")

                                        encrypt_name = input("введите имя для зашифрованного файла формата .encrypt ")

                                        z1_1 += check_errors_encrypt_name_write(encrypt_name, z1)
                                        if z1_1 > z1:
                                            z1 = z1_1
                                            continue

                                        encryptpath = os.path.join(folderpath, encrypt_name) 
                                        try:    
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
                                            break
                                        except FileNotFoundError:
                                            print("файл нот фаундб сори")
                                            z1 += 1
                                            print("неверный ввод, до выхода из программы осталось ", (3 - z1),"попыток")  
                                        except Exception:
                                            z1 += 1
                                            print("неверный ввод, до выхода из программы осталось ", (3 - z1),"попыток")  

                                elif num_of_shifr == 2: # перестановка
                                    z2 = 0
                                    z2_2 = 0
                                    while z2 < 3:
                                        filepath = input("введите путь к тексту   ")

                                        z2_2 += check_errors_filepath(filepath, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue

                                        key_name = input("введите имя ключа шифрования  ")
                                        
                                        z2_2 += check_errors_key_name_read(key_name, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue
                                        
                                        keypath = os.path.join(folderpath, key_name)
                                        
                                        key_perestanovka = []
                                        try:    
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
                                        except FileNotFoundError:
                                            print("нет файла, введите путь заново")
                                            z2 += 1
                                            print("неверный ввод, до выхода из программы осталось ", (3 - z2),"попыток")

                                        
                                        encrypt_name = input("введите имя для зашифрованного файла формата .encrypt ")

                                        z2_2 += check_errors_encrypt_name_write(encrypt_name, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue
                                        
                                        encryptpath = os.path.join(folderpath, encrypt_name)
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
                                        break

                                elif num_of_shifr == 3: # гаммирование
                                    z3 = 0
                                    z3_3 = 0
                                    while z3 < 3:
                                        filepath = input("введите путь к тексту   ")

                                        z3_3 += check_errors_filepath(filepath, z3)
                                        if z3_3 > z3:
                                            z3 = z3_3
                                            continue

                                        keypath = input("введите путь к ключу шифрования  ")
                                        
                                        z3_3 += check_errors_key_name_read(keypath, z3)
                                        if z3_3 > z3:
                                            z3 = z3_3
                                            continue

                                        key_gamm = []
                                        try:
                                            with open(keypath, "r", encoding="utf-8" ) as key:
                                                check_phrase_shifr_gammirovanie = "key_gammirovanie\n"
                                                first_line = key.readline()
                                                if first_line != check_phrase_shifr_gammirovanie:
                                                    print('wrong key')
                                                    break
                                                else:
                                                    print ('проверка на ключ шифра: успешно')
                                                for temp_line in key:
                                                    temp_line = temp_line.split(' ')
                                                    temp_line.pop()
                                                    key_gamm.extend(temp_line)
                                        except FileNotFoundError:
                                            z3 += 1
                                            print("нет файла, введите путь заново")
                                            print("неверный ввод, до выхода из программы осталось ", (3 - z1),"попыток")
                                            continue

                                        encryptpath = input("введите имя для зашифрованного файла формата .encrypt ")

                                        z3_3 += check_errors_encrypt_name_write(encryptpath, z3)
                                        if z3_3 > z3:
                                            z3 = z3_3
                                            continue

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
                                        break
                                elif num_of_shifr == 4:
                                    break

                        elif num1_1 == 2: #зашифровать/расшифровать -> расшифровать
                            print(".>> выберите метода дешифровки")
                            print(".>> 1) замена")
                            print(".>> 2) перестановка")
                            print(".>> 3) гамирование")
                            print(".>> 4) выход")

                            num_of_deshifr = input("выберите метод шифрования:...")

                            check_flag = pr_num1_3(num_of_deshifr)
                            if check_flag == False:
                                z += 1
                                print("неверный ввод, до выхода из программы осталось ", (3 - z),"попыток")
                            else:
                                num_of_deshifr = int(num_of_deshifr)
                                if num_of_deshifr == 1: #расшифровать замена
                                    z1 = 0
                                    z1_1 = 0
                                    while z1 < 3:
                                        filepath = input("введите путь к тексту   ")

                                        z1_1 += check_errors_filepath(filepath, z1)
                                        if z1_1 > z1:
                                            z1 = z1_1
                                            continue

                                        
                                        key_name = input("введите имя ключа шифрования  ")
                                        
                                        z1_1 += check_errors_key_name_read(key_name, z1)
                                        if z1_1 > z1:
                                            z1 = z1_1
                                            continue
                                        
                                        keypath = os.path.join(folderpath, key_name)

                                        bukvi_orig = []
                                        bukvi_encrypt = []

                                        try:   
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
                                        except FileNotFoundError:
                                            z1 += 1
                                            print("нет файла, введите путь заново")
                                            continue

                                        encrypt_name = input("введите путь для файла формата .encrypt ")

                                        z1_1 += check_errors_encrypt_name_read(encrypt_name, z1)
                                        if z1_1 > z1:
                                            z1 = z1_1
                                            continue
                                        
                                        encryptpath = os.path.join(folderpath, encrypt_name)
                                        
                                        shifr_text_zamena = []

                                        try:   
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
                                        
                                        except FileNotFoundError:
                                            z1 += 1
                                            print("нет файла, введите путь заново")
                                            print("неверный ввод, до выхода из программы осталось ", (3 - z1),"попыток")

                                        decrypt_name = input("название_расшифрованного_файла.txt... ") 

                                        z1_1 += check_errors_decrypt_name_write(decrypt_name, z1)
                                        if z1_1 > z1:
                                            z1 = z1_1
                                            continue

                                        decryptpath = os.path.join(folderpath, decrypt_name) 

                                        try:
                                            obj1 = shifr_zamena()
                                            open_text = obj1.read_text(filepath)
                                            key_decrypt = obj1.generate_key_decrypt_zamena(bukvi_orig,bukvi_encrypt)
                                            deshifr_text_zamena = obj1.generate_deshifr_text_zamena(key_decrypt,shifr_text_zamena) #расшифровали

                                            with open(decryptpath, "w", encoding="utf-8" ) as decryptedtext:
                                                for i in range(len(deshifr_text_zamena)):
                                                    decryptedtext.write(deshifr_text_zamena[i])
                                            print('текст расшифрован')
                                            break
                                        except FileNotFoundError:
                                            z1 += 1
                                            print("нет файла, введите путь заново")
                                            print("неверный ввод, до выхода из программы осталось ", (3 - z1),"попыток")
                                            continue

                                elif num_of_deshifr == 2: #расшифровать перестановка        
                                    z2 = 0
                                    z2_2 = 0
                                    while z2 < 3:
                                        filepath = input("введите путь к тексту   ")

                                        z2_2 += check_errors_filepath(filepath, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue

                                        key_name = input("введите имя ключа шифрования  ")
                                        
                                        z2_2 += check_errors_key_name_read(key_name, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue
                                        
                                        keypath = os.path.join(folderpath, key_name)

                                        key_perestanovka = []
                                        
                                        try:
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
                                        except FileNotFoundError:
                                            z2 += 1
                                            print("нет файла, введите путь заново")
                                            continue

                                        encrypt_name = input("введите путь для файла формата .encrypt ")

                                        z2_2 += check_errors_encrypt_name_read(encrypt_name, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue
                                        
                                        encryptpath = os.path.join(folderpath, encrypt_name)

                                        shifr_text_perestanovka = []

                                        try:
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
                                        except FileNotFoundError:
                                            z2 += 1
                                            print("нет файла, введите путь заново")
                                            print("неверный ввод, до выхода из программы осталось ", (3 - z2),"попыток")

                                        decrypt_name = input("название_расшифрованного_файла.txt... ") 

                                        z2_2 += check_errors_decrypt_name_write(decrypt_name, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue

                                        decryptpath = os.path.join(folderpath, decrypt_name) 

                                        key_len_perestanovka = len(key_perestanovka)
                                        obj2 = shifr_perestanovka()
                                        try:
                                            open_text = obj2.read_text(filepath)
                                            deshifr_text_perestanovka = obj2.generate_deshifr_text_perestanovka(open_text,key_len_perestanovka,shifr_text_perestanovka,key_perestanovka)
                                            with open(decryptpath, "w", encoding="utf-8" ) as decryptedtext:
                                                for i in range(len(deshifr_text_perestanovka)):
                                                    decryptedtext.write(deshifr_text_perestanovka[i])
                                            print(" расшифрованно успешно смотрите результаты в файле с названием " + decryptpath)
                                            break                                       
                                        except FileNotFoundError:
                                            z1 += 1
                                            print("нет файла, введите путь заново")
                                            print("неверный ввод, до выхода из программы осталось ", (3 - z1),"попыток")
                                            continue

                                elif num_of_deshifr == 3: #расшифровать гаммирование
                                    z2 = 0
                                    z2_2 = 0
                                    while z2 < 3:
                                        filepath = input("введите путь к тексту   ")

                                        z2_2 += check_errors_filepath(filepath, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue
                                        
                                        key_name = input("введите имя ключа шифрования  ")
                                        
                                        z2_2 += check_errors_key_name_read(key_name, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue
                                        
                                        keypath = os.path.join(folderpath, key_name)

                                        key_gamm = []

                                        try:  
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
                                        except FileNotFoundError:
                                            z2 += 1
                                            print("нет файла, введите путь заново")
                                            continue

                                        encrypt_name = input("введите путь для файла формата .encrypt ")

                                        z2_2 += check_errors_encrypt_name_read(encrypt_name, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue
                                        
                                        encryptpath = os.path.join(folderpath, encrypt_name)

                                        shifr_text_gamm = []

                                        try:
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
                                        except FileNotFoundError:
                                            z2 += 1
                                            print("нет файла, введите путь заново")
                                            continue

                                        decrypt_name = input("название_расшифрованного_файла.txt... ") 

                                        z2_2 += check_errors_decrypt_name_write(decrypt_name, z2)
                                        if z2_2 > z2:
                                            z2 = z2_2
                                            continue

                                        decryptpath = os.path.join(folderpath, decrypt_name) 

                                        obj3 = shifr_gammirovanie()
                                        open_text = obj3.read_text(filepath)
                                        deshifr_text_gamm = obj3.generate_deshifr_text_gammirovanie(open_text,key_len_gamm,bukvi_orig_gamm,key_gamm,shifr_text_gamm)

                                        with open(decryptpath, "w", encoding="utf-8" ) as decryptedtext:
                                            for i in range(len(deshifr_text_gamm)):
                                                decryptedtext.write(deshifr_text_gamm[i])
                                        print('текст расшифрован')
                                        break

                                elif num_of_deshifr == 4:
                                    break
                        elif num1_1 == 3:
                            y = 3
                            break    

            elif num1 == 2: #сгенерировать ключ
                print(".>> Сгенерировать ключ для следующего алгоритма: ")
                print(".>> 1) шифр замены")
                print(".>> 2) шифр перестановки")
                print(".>> 3) шифр гаммирования")
                print(".>> 4) выход")
                
                t = 0
                while t < 3:
                    num_of_shifr = (input("выберите метод шифрования:..."))
                    check_flag = pr_num1_3(num_of_shifr)
                    if check_flag == False:
                        t += 1
                        print("неверный ввод, до выхода из программы осталось ", (3 - t),"попыток")
                    else:
                        num_of_shifr = int(num_of_shifr)
                        if num_of_shifr == 1: # шифр замена
                            t1 = 0
                            t1_1 = 0
                            while t1 < 3:
                                filepath = input("введите путь к тексту   ")

                                t1_1 += check_errors_filepath(filepath, t1)
                                if t1_1 > t1:
                                    t1 = t1_1
                                    continue
                                                                
                                obj1 = shifr_zamena()
                                try:    
                                    open_text = obj1.read_text(filepath)
                                    bukvi_orig = obj1.generate_alphabet_zamena(open_text)
                                    bukvi_encrypt = obj1.generate_key_zamena(bukvi_orig)
                                    key_decrypt = obj1.generate_key_decrypt_zamena(bukvi_orig,bukvi_encrypt)
                                    key_encrypt = obj1.generate_key_encrypt_zamena(bukvi_orig,bukvi_encrypt)

                                except FileNotFoundError:
                                    print("файл не найден, повторите ввод")
                                    t1 += 1
                                    continue
                                
                                
                                key_name = input("введите имя ключа шифрования  ")

                                t1_1 += check_errors_key_name_write(key_name, t1)
                                if t1_1 > t1:
                                    t1 = t1_1
                                    continue

                                keypath = os.path.join(folderpath, key_name)

                            
                                with open(keypath, "w", encoding="utf-8" ) as key:
                                    check_phrase_shifr_zamena = "key_zamena\n"
                                    key.write(check_phrase_shifr_zamena)
                                    for key1 in key_encrypt:
                                        line = key1 + ' ' + key_encrypt[key1] + '\n'
                                        key.write(line)
                                print("the key has been succesfully saved ...")
                                t = 3
                                y = 3
                                break
                                
                        elif num_of_shifr == 2: # шифр перестановка
                            t1 = 0
                            t1_1 = 0
                            while t1 < 3:
                                key_len_perestanovka = (input("enter key length... (int number) "))
                                #для отрицательных чисел только, специально обрезаю минус слева
                                key_len_perestanovka_bootleg = key_len_perestanovka.lstrip("-")
                                if key_len_perestanovka_bootleg.isnumeric() == False:
                                    print("введите целое число")
                                    t1 += 1
                                    print("неверный ввод у вас осталось ", (3 - t1), "попыток")
                                    continue
                                key_len_perestanovka = int(key_len_perestanovka)
                                if key_len_perestanovka < 1:
                                    print("не может быть отрицательным")
                                    t1 += 1
                                    print("неверный ввод у вас осталось ", (3 - t1), "попыток")
                                    continue
                                
                                
                                try:
                                    obj2 = shifr_perestanovka()
                                    key_perestanovka = obj2.generate_key_perestanovka(key_len_perestanovka)
                                except FileNotFoundError:
                                    print("файл не найден, повторите ввод")
                                    t1 += 1
                                    continue

                                key_name = input("введите имя ключа шифрования  ")

                                t1_1 += check_errors_key_name_write(key_name, t1)
                                if t1_1 > t1:
                                    t1 = t1_1
                                    continue
                                
                                keypath = os.path.join(folderpath, key_name)
                                with open(keypath, "w", encoding="utf-8" ) as key:
                                    check_phrase_shifr_perestanovka = "key_perestanovka\n"
                                    key.write(check_phrase_shifr_perestanovka)
                                    for i in range(len(key_perestanovka)):
                                        tmp_l = str(key_perestanovka[i]) + '\n'
                                        key.write(tmp_l)

                                print("the key has been succesfully saved ...")
                                t = 3
                                y = 3
                                break

                        elif num_of_shifr == 3: # шифр гамирование
                            t3 = 0
                            t3_3 = 0
                            while t3 < 3:
                                filepath = input("введите путь к тексту   ")

                                t3_3 += check_errors_filepath(filepath, t3)
                                if t3_3 > t3:
                                    t3 = t3_3
                                    continue

                                key_len_gamm = (input("enter key length... (int number) "))
                                #для отрицательных чисел только, специально обрезаю минус слева
                                key_len_gamm_bootleg = key_len_gamm.lstrip("-")
                                if key_len_gamm_bootleg.isnumeric() == False:
                                    print("введите целое число")
                                    t3 += 1
                                    t3_3 += 1
                                    print("неверный ввод, до выхода из программы осталось ", (3 - t3),"попыток")
                                    continue
                                key_len_gamm = int(key_len_gamm)
                                if key_len_gamm < 1:
                                    print("число не должно быть отрицательным")
                                    t3 += 1
                                    t3_3 += 1
                                    print("неверный ввод, до выхода из программы осталось ", (3 - t3),"попыток")
                                    continue
                                
                                
                                obj3 = shifr_gammirovanie()
                                try:
                                    open_text = obj3.read_text(filepath)
                                    bukvi_orig_gamm = obj3.generate_alphabet_gammirovanie(open_text)
                                    key_gamm = obj3.generate_key_gamm(key_len_gamm,bukvi_orig_gamm)
                                except FileNotFoundError:
                                    print("файл не найден, повторите ввод")
                                    t3 += 1
                                    continue

                                key_name = input("введите имя ключа шифрования  ")

                                t3_3 += check_errors_key_name_write(key_name, t3)
                                if t3_3 > t3:
                                    t3 = t3_3
                                    continue

                                keypath = os.path.join(folderpath, key_name)
                                
                                with open(keypath, "w", encoding="utf-8" ) as key:
                                    check_phrase_shifr_gammirovanie = "key_gammirovanie\n"
                                    key.write(check_phrase_shifr_gammirovanie)
                                    for i in range(len(key_gamm)):
                                        tmp_l = str(key_gamm[i]) + ' '
                                        key.write(tmp_l)

                                print("the key has been succesfully saved ...")
                                t = 3
                                y = 3
                                break

                        elif num_of_shifr == 4:
                            y = 3
                            break

            elif num1 == 3:
                x = 3
                break





