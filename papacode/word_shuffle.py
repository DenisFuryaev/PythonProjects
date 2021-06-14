import re
import string

def dict_from_str(str):
    dict = {}
    for char in str:
        if char in ',.!?':
            if char in dict:
                dict[char] = dict[char] + 1
            else:
                dict[char] = 1

    for word in re.split('[ ,.!?]+', str.lower()):
        if len(word) == 0:
            continue
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    return dict

str_1 = input()
str_2 = input()

a = dict_from_str(str_1)
b = dict_from_str(str_2)

print(a == b)

