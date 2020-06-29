import os
from security_lab4 import *


def writing(user_name: str, hashed_password: str, user_folder: str,
            master_key: str) -> None:
    name = "db.txt"
    location = os.getcwd()
    store_path = os.path.join(location, name)
    with open(store_path, "a", encoding='utf-8') as file:
        file.write(user_name)
        file.write('\n')
        file.write(hashed_password)
        file.write('\n')
        file.write(user_folder)
        file.write('\n')
        file.write(master_key)
        file.write('\n')
    return None


def checking_for_login(user_name):
    name = "db.txt"
    location = os.getcwd()
    store_path = os.path.join(location, name)
    flag = os.path.isfile(store_path)
    if flag is False:
        print("вы первый пользователь")
        return True
    with open(store_path, "r", encoding='utf-8') as file:
        for i in file:
            tmp = i.rstrip("\n")
            if user_name == tmp:
                print("пользователь с таким именем уже существует")
                return False
    return True


def check_exists_db():
    name = "db.txt"
    location = os.getcwd()
    store_path = os.path.join(location, name)
    if os.path.isfile(store_path) is False:
        data = []
        err = 'err'
        data.append(err)
        return data
    else:
        data = []
        no_err = '0'
        data.append(no_err)
        return data


def check_user_exists(user_name):
    user_name += '\n'
    name = "db.txt"
    location = os.getcwd()
    store_path = os.path.join(location, name)
    with open(store_path, "r", encoding='utf-8') as file:
        for i in file:
            if i == user_name:
                return True
    return False


def collecting_information(user_name):
    name = "db.txt"
    location = os.getcwd()
    store_path = os.path.join(location, name)
    with open(store_path, "r", encoding='utf-8') as file:
        data = []
        for i in file:
            login = i.strip("\n")
            if login == user_name:
                data.append(login)
                password = file.readline()
                tmp = password.rstrip("\n")
                data.append(tmp)
                folder = file.readline()
                tmp = folder.rstrip("\n")
                data.append(tmp)
                master_key = file.readline()
                tmp = master_key.rstrip("\n")
                data.append(tmp)
                return data


def delete_account(user_name):
    name = "db.txt"
    location = os.getcwd()
    store_path = os.path.join(location, name)
    new_name = "new_db.txt"
    new_store_path = os.path.join(location, new_name)
    with open(store_path, 'r', encoding='utf-8') as file:
        for line in file:
            data_tmp = []
            data_tmp.append(line)
            str_tmp = file.readline()
            data_tmp.append(str_tmp)
            str_tmp = file.readline()
            data_tmp.append(str_tmp)
            str_tmp = file.readline()
            data_tmp.append(str_tmp)
            log_check = data_tmp[0]
            log_check = log_check.rstrip("\n")
            if log_check != user_name:  # replace with user_name
                with open(new_store_path, 'a', encoding='utf-8') as newfile:
                    newfile.writelines(data_tmp)

    folder_path = os.path.join(location, user_name)
    try:
        os.rmdir(folder_path)
    except OSError:
        tmp = whats_in_folder(folder_path)
        for i in range(len(tmp)):
            tmp_name = tmp[i]
            tmp_file = os.path.join(folder_path, tmp_name)
            os.remove(tmp_file)

    os.remove(store_path)
    try:
        os.rename(new_store_path, store_path)
    except FileNotFoundError:
        print("вы удалили последнего пользователя")


def change_key_shifr(user_name):
    data = collecting_information(user_name)
    user_password = data[1]
    user_password = user_password.rstrip("\n")  # получили пароль

    user_folder = data[2]  # получили папку
    user_master_key_str = data[3]
    user_master_key_str = user_master_key_str.rstrip("\n")
    user_master_key = bytes.fromhex(user_master_key_str)

    user_password_bytes = bytes(user_password, 'utf-8')

    master_klyuchik = gen_user_secret_key(user_password_bytes)
    master_klyuchik_str = master_klyuchik.hex()
    master_klyuchik = bytes.fromhex(master_klyuchik_str)
    real_master_key = decrypt(user_master_key, master_klyuchik)

    new_klychik = gen_secret_key()
    new_master_klychik = gen_user_secret_key(user_password_bytes)

    # !!!
    new_master_key = encrypt(new_klychik, new_master_klychik)
    new_master_key_str = new_master_key.hex()

    notes_arr = os.listdir(user_folder)
    for note_name in notes_arr:
        note_path = os.path.join(user_folder, note_name)
        with open(note_path, 'r', encoding='utf-8') as file:
            enc_note_hex = file.read()
        enc_note_bytes = bytes.fromhex(enc_note_hex)
        dec_note_bytes = decrypt(enc_note_bytes, real_master_key)
        enc_new_note_bytes = encrypt(dec_note_bytes, new_klychik)
        enc_new_note_str = enc_new_note_bytes.hex()
        with open(note_path, "w", encoding='utf-8') as file:
            file.write(enc_new_note_str)

    name = "db.txt"
    location = os.getcwd()
    store_path = os.path.join(location, name)
    new_name = "new_db.txt"
    new_store_path = os.path.join(location, new_name)
    with open(store_path, 'r', encoding='utf-8') as file:
        old_data = file.read()

    what_changes = data[3]
    what_replaces = new_master_key_str

    new_data = old_data.replace(what_changes, what_replaces)

    with open(new_store_path, 'w', encoding='utf-8') as file:
        file.write(new_data)

    os.remove(store_path)
    os.rename(new_store_path, store_path)


def whats_in_folder(user_folder):
    arr = os.listdir(user_folder)
    return arr


if __name__ == "__main__":
    pass
