#!/usr/bin/python3


def print_args(*args):
    number_of_args = len(args)
    key_word = 'argument'
    if number_of_args > 1:
        key_word = 'arguments'
    print(f"{number_of_args}: {key_word}")
    for index, item in enumerate(args, start=1):
        print(f"{index}: {item}")

if __name__=='__main__':
    print_args()
