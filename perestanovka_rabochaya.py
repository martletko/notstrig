import random

key_len = int(input("enter key length... (int number) "))

key = []
for i in range(1,key_len + 1): 
    key.append(i)
    
random.shuffle(key) 

with open("lab3/otkrytii_tekst.txt", "r", encoding="utf-8") as file:
    open_text = list(file.read())
print(open_text)

while len(open_text) % key_len != 0:
    open_text.append(' ')

shifr_text = []

for i in range(0 ,len(open_text) , key_len):
    temp_list = open_text[i:i+key_len]
    temp_list_mask = temp_list.copy()
    for k in range(key_len):
        temp_num = int(key[k])
        temp_list_mask[k] = temp_list[temp_num - 1]
    shifr_text.extend(temp_list_mask)

deshifr_text = []

for i in range(0 ,len(open_text) , key_len):
    temp_list = shifr_text[i:i+key_len]
    temp_list_mask = temp_list.copy()
    for k in range(key_len):
        temp_num = int(key[k])
        temp_list_mask[temp_num-1] = temp_list[k]
    deshifr_text.extend(temp_list_mask)

print(str(deshifr_text))