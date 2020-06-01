def check():    
    filepath = input("enter path to txt.txt... ")
    check_filepath = filepath.split('.')
    if check_filepath[-1] != 'txt':
        print("wrong txt format")
        break
    print("проверка на расширение текстоового файла: успешно")

    keypath = input("enter path to key.key... ")

    check_key = keypath.split('.')
    if check_key[-1] != 'key':
        print("wrong key format")
        break
    print('проверка на расширение ключа: успешно')   

    encryptpath = input("enter path to encrypttext.encrypt ... ")

    check_shifrtext = encryptpath.split('.')
    if check_shifrtext[-1] != 'encrypt':
        print('wrong encrypted_text_format')
        break
    print("проверка на расширение зашифрованного текста: успешно") 

    decryptpath = input("enter path to decrypttext.txt...  ")

    check_deshifr = decryptpath.split('.')
    if check_deshifr[-1] != 'txt':
        print('wrong decrypted_text_format')
        break
    print("проверка на расширение расшифрованного текста: успешно") 
    return None

while True:
    y = check()
    


