#!/usr/bin/python3

def remove_char_at(str, n):
    if n < len(str) and n >= 0:
        aux = str.replace(str[n], "")
        return aux
    else:
        return str


remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
