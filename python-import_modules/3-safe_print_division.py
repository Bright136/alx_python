#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = int(a)/int(b)
    except ZeroDivisionError:
        result = None
    except ValueError:
        print('Invalid input: Number is not an integer')
    finally:
        print(f"Inside result: {result}")
        return result

a = 12
b = 2

result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0

result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

