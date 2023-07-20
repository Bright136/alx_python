#!/usr/bin/env python3

def validate_password(password):
    has_lower_case = any(char.islower() for char in password)
    has_upper_case = any(char.isupper() for char in password)
    has_number = any(char.isdigit() for char in password)
    len_ = len(password) >= 8
    does_not_contain_space = ' ' not in password

    print(password, has_lower_case, has_upper_case, has_number, len_, does_not_contain_space)
    return has_lower_case and has_upper_case and has_number and len_ and does_not_contain_space


# test 

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
