#!/usr/bin/python3

def multiple_returns(sentence):
    first_char = sentence[0] if sentence else None
    return len(sentence), first_char

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

