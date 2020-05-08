def repeat():
    i=0
    while flag:
     command_continue = input("Продолжить? Д/Н...")
     if command_continue == "Д":
            return True
     elif command_continue == "Н":
            return False
     elif i<3:
            i+=1
            print("Wrong input")
     if i==3:
        print("Too much errors in input")
        return False



data = [] # в него летят все параметры и их значения
with open("conf", "r") as file:
    for line in file:
        if line[0] != '#' and line[0] != ';' and line[0] != '\n':
            data.append(line)


data1 = [] # в него летят обработанные параметр и значение



for i in range(len(data)):
    tmp_str = data[i]
    if ' ' in tmp_str:
        tmp_str = tmp_str.replace('\n','') 
        tmp_str = tmp_str.split(' ',1)
        data1.append(tmp_str)

    else:
        tmp_str = tmp_str.replace('\n','') 
        tmp_str += ' Нет Данных'
        tmp_str = tmp_str.split(' ',1)
        data1.append(tmp_str)

users_dict = dict(data1) # здесь мальчики становятся мужчинами, кхм, списки словарями

''' НАЧАЛО РАБОТЫ С ПОЛЬЗОВАТЕЛЕМ'''

flag = True


print("Хеллоу юзер\n")
print("перед тобой список команд которые я вытащил из файла conf\n")

print("**********НАЧАЛО ПАРАМЕТРОВ**********\n")

for key in (users_dict.keys()):
    print(key,"\n")

print("**********КОНЕЦ ПАРАМЕТРОВ**********\n")

print("прошу тебя выбери нужный параметр (1 слово) (они все 1 слово) и правильно его напиши\n")

while(flag):    
    
    command = input("Get param...")

    if command in users_dict:
        value = users_dict[command]
        print(value)
        flag=repeat()
    else:
        print("Элемент не найден")
        flag=repeat()