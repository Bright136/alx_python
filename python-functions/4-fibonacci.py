#!/usr/bin/env python3

def fibonacci_sequence(n):
    list = []
    for i in range(n):
        if i <= 1:
            f = i
        else:
            f = list[(i-1)] + list[(i - 2)]
        list.append(f)
    return list
