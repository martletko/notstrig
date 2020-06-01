import random

for i in range(10):
    print(i,":", random.randint(1,10))

data = [1,2,3,4,5]

random.shuffle(data)

print(data)


'''
как сделать так чтобы через рандинт не было повторений 
'''

#как работает рандинт
key = []
key_len = 10
while True:
    new_val = random.randint(1,10)
    if new_val in key:
        print("debug!")
    else:
        key.append(new_val)
    if len(key) == key_len:
        break
print(key)

#через шафл
key_len = input("введите длину ключа...") # только число
key1 = []
for i in range(1,int(key_len)+1):
    new_val = i
    key1.append(new_val)
    random.shuffle(key1)
print(key1)


'''
чтобы сгенерировать случайные позиции для шифра можно испольщовать метод рандом
random.randint И random.shuffle 
лучше работать через шафл 
'''
#через рандинт
key2 = []
key_len = 10
data = [1,2,3,4,5,6,7,8,9,10]
while True:
    index = random.randint(0,len(data) - 1)
    new_val = data[index]
    key2.append(new_val)
    del data[index]
    if len(data) == 0:
        break
print(key2)

# для ключа замены 

key2 = []
key_len = 10
data = ["а","б","в","г","д","е","ё","ж","з","и"]  #вмпсто ключа замены будет алфавит
old_data = data.copy()
while True:
    index = random.randint(0,len(data) - 1)
    new_val = data[index]
    key2.append(new_val)
    del data[index]
    if len(data) == 0:
        break
print(old_data)
print(key2)

#через шафл
random.shuffle(old_data)
print(old_data)


#как создать список из элементов длиной в кей лен
key = []
for i in range(key_len):
    key.append(i)

#есть еще генераторы списков #я_и_бал
key_len = 10
doubles = [n for n in range(key_len)]
print(doubles)




