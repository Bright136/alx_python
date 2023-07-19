#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
def get_lastnumber(num):
    last_digit = abs(num) % 10
    return last_digit if num >= 0 else -last_digit

last_number = get_lastnumber(number)

if last_number == 0:
    print("Last digit of {} is {} and is 0".format(number, last_number))
elif last_number > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_number))
elif last_number < 5:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_number))





    