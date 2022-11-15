#!/usr/bin/python

# ----------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# date: dd-MM-yyyy
# description: simple python script
# ----------------------------------------------------------

USERNAME_FILE = 'Users.txt'


# ---------------------------------------------------------
# clean passed string removind break lines and spaces
def clean_string(string: str):
    cleaned_string = string.replace('\n', '')
    return cleaned_string


# ---------------------------------------------------------
# based on Users file generates names
new_name = (clean_string(name) for name in open(USERNAME_FILE))

for i in range(10):
    print(next(new_name))
