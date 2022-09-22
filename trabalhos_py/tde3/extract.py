#!/usr/bin/python

# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# ------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# import section
import os
from email.parser import BytesParser
from email import policy


# ---------------------------------------------------------------------------------------------------------------------
# const sections
#dataset_path = './dataset/'


# ---------------------------------------------------------------------------------------------------------------------
# global variables
#files = []
#objects = {}


# ---------------------------------------------------------------------------------------------------------------------
# this will get all paths from data files
# return: list of file paths
def list_files(current_path: str = './', files: list = []):
    for element in os.listdir(current_path):
        f = current_path+element
        if os.path.isdir(f):
            list_files(f+'/')
        if os.path.isfile(f):
            files.append(f)
    return files

# ---------------------------------------------------------------------------------------------------------------------
# create objects dict with
# return: JSON dict with JSON objects
def mount_objects(files: list = []):
    objects = {}
    for file in files:
        with open(file, 'rb') as fp:
            msg = BytesParser(policy=policy.default).parse(fp)
            _from = msg['From']
            _from = _from.strip()
            if msg['To'] != None:
                to = msg['To'].split(',')
            else:
                to = []
            if _from not in objects:
                objects[_from] = {}
            for _to in to:
                _to = _to.strip()
                if '' != _to:
                    if _to not in objects[_from]:
                       objects[_from][_to] = 1
                    else:
                        objects[_from][_to] = objects[_from][_to]+1
            fp.close()
    return objects