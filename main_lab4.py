import os
from security_lab4 import *
from db_lab4 import *
from notes_lab4 import *


def pr_num1_2(num):
    if num.isnumeric() == True:
        num = int(num)
        if num == 1 or num == 2: 
            return True
        if num != 1 and num != 2:
            print("число должно быть или 1 или 2 or 3")
        return False
    else:
        print("введите целое число  ")
        return False

def check_empty_name(user_input):
    if user_input == "":
        return False
    return True

def check_symbols(user_input):
    error_symbols = ["\\","/",":", "*","?","\"","|", "<",">"]
    for i in user_input:
        if error_symbols.count(i) != 0:
            print("неверный символ в названии проверьте  чтобы таких символов не было /  : * ? | < >  ")
            return False
    
    if error_symbols.count(i) == 0:
        return True

def pr_num_1_9(num):
    if num.isnumeric() == True:
        num = int(num)
        arr = [1,2,3,4,5,6,7,8,9]
        for i in range(len(arr)):
            if num in arr:
                return True
            else:
                print("введите целое число от 1 до 9")
                return False
    else:
        return False

program_folder_location = os.getcwd()
x = 0
while x < 3:
    print("Главное меню")
    print("1) Зарегестрироваться")
    print("2) Войти")

    num1 = input("Выберите пункт меню...  ")
    check_flag = pr_num1_2(num1)
    if check_flag == False:
        x += 1
        print("неверный ввод, у вас осталось ", (3 - x), "попыток")
        continue
    else:
        num1 = int(num1)
    
    if num1 == 1:
        print("Регистрация")
        user_name = input("Введите имя пользователя   ")


        check_flag = checking_for_login(user_name)
        if check_flag == False:
            x += 1
            print("неверный ввод, у вас осталось ", (3 - x), "попыток")
            continue

        check_flag = check_empty_name(user_name) 
        if check_flag == False:
            x += 1
            print("неверный ввод, у вас осталось ", (3 - x), "попыток")
            continue
        check_flag = check_symbols(user_name) 
        if check_flag == False:
            x += 1
            print("неверный ввод, у вас осталось ", (3 - x), "попыток")
            continue        
        
        user_password = input("введите пароль...   ") # записываем в файлик

        check_flag = check_empty_name(user_password) 
        if check_flag == False:
            x += 1
            print("неверный ввод, у вас осталось ", (3 - x), "попыток")
            continue
        check_flag = check_symbols(user_password) 
        if check_flag == False:
            x += 1
            print("неверный ввод, у вас осталось ", (3 - x), "попыток")
            continue 


        bytes_user_password = bytes(user_password, encoding = 'utf-8')
        hashed_password = hash_value(bytes_user_password)
        hashed_password = bytes(hashed_password,encoding='utf-8')

        #создаем папку
        user_folder = os.path.join(program_folder_location, user_name)
        os.mkdir(user_folder)

        #сгенерировали ключик шифрования (ранд байты)
        klyuchik = gen_secret_key()

        #генерируем ключ на основе пользовательского пароля (мастер кей)
        master_klyuchik = gen_user_secret_key(hashed_password)
        hashed_password = hashed_password.decode('utf-8')

        master_key = encrypt(klyuchik, master_klyuchik) # зашифровали рандомные байты на основе ключа от польз пароля
        master_key = master_key.hex()


        #записали все данные в текстовик
        writing(user_name,hashed_password,user_folder,master_key)
        
        continue

    elif num1 == 2:
        print("Вход")

        check_flag = check_exists_db()
        if check_flag[0] == 'err':
            x += 1
            print("еще не ни одного зарегестрированного пользователя, зарегестрируйтесь")
            print("ошибка, у вас осталось ", (3 - x), "попыток")
            continue

        login_input = input("Введите логин...   ")

        check_flag = check_empty_name(login_input) 
        if check_flag == False:
            x += 1
            print("неверный ввод, у вас осталось ", (3 - x), "попыток")
            continue
        check_flag = check_symbols(login_input) 
        if check_flag == False:
            x += 1
            print("неверный ввод, у вас осталось ", (3 - x), "попыток")
            continue   

        data = collecting_information(login_input)   
        if data[0] == 'wrong_name':
            print("Такого пользователя у нас еще нет, зарегистрируйтесь")
            x += 1
            print("неверный ввод, у вас осталось ", (3 - x), "попыток")
            continue   

        input_password = input("введите пароль...  ")
        input_password = bytes(input_password, encoding = 'utf-8')
        hashed_input_password = hash_value(input_password)


        user_name = data[0]
        user_name.rstrip("\n")
        user_password = data[1]
        user_password.rstrip("\n")
        
        if user_password == hashed_input_password:
            print("пароль верный")
        else:
            print("пароль не верный")
            x += 1
            print("неверный ввод, у вас осталось ", (3 - x), "попыток")
            continue

        user_password = bytes(user_password, 'utf-8')

        user_folder = data[2]
        user_folder = user_folder.rstrip('\n')
        master_key = data[3]
        master_key = bytes.fromhex(master_key)

        master_klyuchik = gen_user_secret_key(user_password)
        master_klyuchik = master_klyuchik.hex()
        master_klyuchik = bytes.fromhex(master_klyuchik)

        real_master_key = decrypt(master_key, master_klyuchik)


        print("меню пользователя ", user_name, ":   ")

        y = 0
        while y < 3:
            print("1) удалить аккаунт")
            print("2) изменить ключ шифрования", "выкидывает в гм") 
            print("РАБОТА С ЗАМЕТКАМИ:     ")
            print("3) создать заметку")
            print("4) изменить заметку")
            print("5) удалить заметку")
            print("6) удалить все заметки")
            print("7) получить список всех заметок")
            print("8) прочитать конкретную заметку")
            print("9) выход в главное меню")

            num2 = input("выберите пункт меню:...   ")
            check_flag = pr_num_1_9(num2)
            if check_flag == False:
                y += 1
                print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                continue
            
            num2 = int(num2)
            if num2 == 1:
                delete_account(user_name)
                break

            if num2 == 2:
                change_key_shifr(user_name)
                break

            if num2 == 3:
                
                note_name = input("введите имя для заметки (без расширения .txt).... ")

                check_flag = check_empty_name(note_name)
                if check_flag == False:
                    y += 1
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue
                
                check_flag = check_symbols(note_name)
                if check_flag == False:
                    y += 1
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue
                note_name = note_name + '.txt'

                arr = os.listdir(user_folder)
                if note_name in arr:
                    print("такая заметка уже существует")
                    y += 1
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue

                main_screen()
                location = os.getcwd()
                name = 'tmp.txt'
                temp_path = os.path.join(location , name)

                if os.path.isfile(temp_path) == False:
                    y += 1
                    print("похоже вы закрыли программу без сохранения изменений")
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue

                with open(temp_path, 'r', encoding='utf-8') as file:
                    text_data = file.read()
                os.remove(temp_path)
                text_data = text_data.encode('utf-8')
                chipher_text_data = encrypt(text_data, real_master_key)
                chipher_text_data = chipher_text_data.hex()
                save_location = os.path.join(user_folder, note_name)
                with open(save_location, "w", encoding='utf-8') as note:
                    note.write(chipher_text_data)
                print("заметка сохранена")
                continue
                
            if num2 == 4:
                arr = os.listdir(user_folder)
                if arr == []:
                    print("заметки отсутствуют")
                    continue
                print("список заметок для редактирования")
                opt_arr = []
                for i in range(len(arr)):
                    print(i+1, ") ", arr[i])
                    tmp = i+1
                    opt_arr.append(tmp)

                inp_num = input("выберите нужную заметку для редактирования   ")

                if inp_num.isnumeric() == False:
                    y += 1
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue
                
                inp_num = int(inp_num)

                if inp_num not in opt_arr:
                    y += 1
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue
                else:
                    note_name_txt = arr[inp_num-1]
                
                note_path = os.path.join(user_folder, note_name_txt)

                with open(note_path, 'r', encoding='utf-8') as file:
                    enc_data = file.read()

                enc_data = bytes.fromhex(enc_data)
                dec_data = decrypt(enc_data, real_master_key)
                dec_data = dec_data.decode('utf-8')
                read_screen(dec_data)

                location = os.getcwd()
                name = 'tmp.txt'
                temp_path = os.path.join(location , name)
                
                if os.path.isfile(temp_path) == False:
                    y += 1
                    print("похоже вы закрыли программу без сохранения изменений")
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue

                with open(temp_path, 'r', encoding='utf-8') as file:
                    text_data = file.read()
                os.remove(temp_path)
                text_data = text_data.encode('utf-8')
                chipher_text_data = encrypt(text_data, real_master_key)
                chipher_text_data = chipher_text_data.hex()
                save_location = note_path
                with open(save_location, "w", encoding='utf-8') as note:
                    note.write(chipher_text_data)
                print("заметка сохранена")
                continue

            if num2 == 5:
                arr = os.listdir(user_folder)
                if arr == []:
                    print("заметки отсутствуют")
                    continue
                print("список заметок для удаления")
                opt_arr = []
                for i in range(len(arr)):
                    print(i+1, ") ", arr[i])
                    tmp = i+1
                    opt_arr.append(tmp)

                inp_num = input("выберите нужную заметку для удаления   ")

                if inp_num.isnumeric() == False:
                    y += 1
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue
                
                inp_num = int(inp_num)

                if inp_num not in opt_arr:
                    y += 1
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue
                else:
                    note_name_txt = arr[inp_num-1]
                
                note_path = os.path.join(user_folder, note_name_txt)
                os.remove(note_path)
                continue

            if num2 == 6:
                tmp = whats_in_folder(user_folder)
                if tmp == []:
                    print("заметки отсутствуют")
                    continue
                for i in range(len(tmp)):
                    tmp_name = tmp[i]
                    tmp_file = os.path.join(user_folder, tmp_name)
                    os.remove(tmp_file)
                tmp = whats_in_folder(user_folder)
                if tmp == []:
                    print("заметки отсутствуют")
                continue

            if num2 == 7:
                tmp = whats_in_folder(user_folder)
                if tmp == []:
                    print("заметки еще не созданы")
                    continue
                print(tmp)
                continue

            if num2 == 8:
                arr = os.listdir(user_folder)
                if arr == []:
                    print("заметки отсутствуют")
                    continue
                print("список заметок для просмотра")
                opt_arr = []
                for i in range(len(arr)):
                    print(i+1, ") ", arr[i])
                    tmp = i+1
                    opt_arr.append(tmp)

                inp_num = input("выберите нужную заметку для просмотра   ")

                if inp_num.isnumeric() == False:
                    y += 1
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue
                
                inp_num = int(inp_num)

                if inp_num not in opt_arr:
                    y += 1
                    print("неверный ввод, у вас осталось ", (3 - y), "попыток")
                    continue
                else:
                    note_name_txt = arr[inp_num-1]
                
                note_path = os.path.join(user_folder, note_name_txt)

                with open(note_path, 'r', encoding='utf-8') as file:
                    enc_data = file.read()

                enc_data = bytes.fromhex(enc_data)
                dec_data = decrypt(enc_data, real_master_key)
                dec_data = dec_data.decode('utf-8')
                print(dec_data)
                continue

            if num2 == 9:
                break







            
                


        

       




        



        
        







