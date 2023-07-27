#!/usr/bin/python3
import sys


def print_args(*args):
    number_of_args = len(args)
    key_word = 'arguments:'
    if number_of_args == 1:
        key_word = 'argument:'
    elif number_of_args == 0:
        key_word = 'arguments.'
    print(f"{number_of_args} {key_word}")
    for index, item in enumerate(args, start=1):
        print(f"{index}: {item}")

if __name__=='__main__':
    arguments = sys.argv[1:]
    print_args(*arguments)
