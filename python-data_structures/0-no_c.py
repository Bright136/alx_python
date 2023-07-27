#!/usr/bin/python3

def no_c(my_string):
    list_string = list(my_string)
    for index, char in enumerate(list_string):
        if char == 'c' or char=='C':
            list_string[index] = ''
    return ''.join(list_string)


print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
            