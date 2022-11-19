# ----------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# date: 15-11-2022
# description: simple python script
# ----------------------------------------------------------
from random import randint
import json
import matplotlib.pyplot as plt
import numpy as np


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
# function to create a generator
# that returns clean string
def clean_generator(file_handler):
    yield (row.strip().split() for row in file_handler)


# -----------------------------------------------
# function that creates a histogram
# of passed data
def new_histogram(
        data_distribution
        , show_mean_indicator: bool
        , mean_value  # only if show_mean_indicator its true
        , y_min  # only if show_mean_indicator its true
        , y_max  # only if show_mean_indicator its true
        , x_label: str
        , y_label: str
):
    plt.hist(data_distribution , edgecolor='black' , alpha=.4)
    if show_mean_indicator:
        # this prints mean marker
        plt.plot([mean_value, mean_value] , [y_min , y_max] , r'--' , label=f'Mean = {mean_value}')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()


# -----------------------------------------------
# function that computes mode from list
def mode(values: list = []):
    # (value, value_freq)
    item = (None, -1)
    verified_values = []
    for value in values:
        if value not in verified_values:
            verified_values.append(value)
            value_freq = values.count(value)
            if value_freq > item[1]:
                item = (value, value_freq)
    return item


# -----------------------------------------------
# function that computes mean value from list
def mean(values: list = []):
    return np.mean(values)


# -----------------------------------------------------------
# iter over dicts from list summing all values from dict keys
# return: int
def sum_list_dicts(some_list: list):
    s = 0
    for element in some_list:
        for key in element:
            s += element[key]
    return s
