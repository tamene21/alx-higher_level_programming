#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for i in range range(len(my_list)):
        if my_list[i] == search:
            copy.append(search)
        else:
            copy.append(my_list[i])
    return copy

