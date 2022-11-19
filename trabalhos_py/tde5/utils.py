# ----------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# date: 15-11-2022
# description: simple python script
# ----------------------------------------------------------
from random import randint
import json


# ---------------------------------------------------------
# clean passed string removing break lines and spaces
def clean_string(string: str):
    cleaned_string = string.replace('\n', '')
    return cleaned_string


# ---------------------------------------------------------
# sort new weight
def new_weight(MIN_W: int = 1, MAX_W: int = 100): return randint(MIN_W, MAX_W)


# ---------------------------------------------------------
# generator for names in Users.txt
NAME_GENERATOR = (clean_string(name) for name in open('Users.txt'))


# ---------------------------------------------------------
# based on Users file generates names
def new_name(): return next(NAME_GENERATOR)


# ---------------------------------------------------------
# min_max scaler
# this will return a value between 0 and 1
def min_max(MIN: float, MAX: float, x: float): return (x - MIN) / (MAX - MIN)


# ---------------------------------------------------------
# verify if passed nodes exists in nodes list
def exists_nodes(verify_nodes: list, nodes_list: list):
    exists = True
    for node in verify_nodes:
        exists = exists and node in nodes_list
    return exists


# -----------------------------------------------
# carregar arquivo JSON para objeto DICT python
def load_json(nome: str = ''):
    with open(nome , 'r') as file:
        python_dict = json.load(file)
    return python_dict


# -----------------------------------------------
# generator for specified file_handler
# that returns clean string
def clean_generator(self, file_handler):
    yield (row.strip().split() for row in file_handler)

