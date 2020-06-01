import random

filepath = "lab3/otkrytii_tekst.txt"
open_text = ""
with open(filepath , "r", encoding="utf-8") as file:
    line = file.readline()
    while line:
        line = line.replace('\n','')
        open_text += line
        line = file.readline()
open_text = list(open_text)

bukvi_orig_gamm = []
for i in open_text:
    if i not in bukvi_orig_gamm:
        bukvi_orig_gamm.append(i)


key_len_gamm = int(input("enter int num key len ..."))


key_gamm = []
while True:
    new_val = random.randint(0, len(bukvi_orig_gamm) - 1)
    if new_val not in key_gamm:
        key_gamm.append(new_val)
    if len(key_gamm) == key_len_gamm:
        break
print(key_gamm)

while len(open_text) % key_len_gamm != 0:
    open_text.append(' ')

shifr_text_gamm = []
for i in range(0 ,len(open_text) , key_len_gamm):
    temp_list = open_text[i:i+key_len_gamm]
    for k in range(key_len_gamm):
        new_index = (bukvi_orig_gamm.index(temp_list[k]) + int(key_gamm[k])) % len(bukvi_orig_gamm)
        temp_list[k] = bukvi_orig_gamm[new_index]
    shifr_text_gamm.extend(temp_list)
print(shifr_text_gamm)

deshifr_text_gamm = []
for i in range(0 ,len(open_text) , key_len_gamm):
    temp_list = shifr_text_gamm[i:i+key_len_gamm]
    for k in range(key_len_gamm):
        new_index = (bukvi_orig_gamm.index(temp_list[k]) - int(key_gamm[k])) % len(bukvi_orig_gamm)
        temp_list[k] = bukvi_orig_gamm[new_index]
    deshifr_text_gamm.extend(temp_list)
print(deshifr_text_gamm)


