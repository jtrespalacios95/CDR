import json
import pandas as pd

file = open("test.txt")
line = file.readline()
head = False
body = False
row = False
row_obj = {}

def get_name(line):
    var = line.split(':')[0]
    return var.replace("'", '')

def get_value(line):
    var = line.split(':')[1]
    return var.replace(',', '')

def insert(key,value):
    if key is not None:
        if key not in row_obj.keys():
            row_obj[key] = value.strip()
        else:
            row_obj [key] = row_obj[key] + ", " + value.strip()


while line != '':

    if 'File start' in line:

        head = True
        line = file.readline()
    if 'End of record' in line and head:
        body = True
        head = False
        linea = file.readline()
    if 'Structure type' in line and body:
        row = True
        insert(get_name(line),get_value(line))
        #linea = file.readline()
    if row:

        if ':' in line and 'Structure type' not in line:
            insert(get_name(line), get_value(line))
    if 'End of' in line and row:
        row = False

    if 'File end' in line:
        head = True
        body = False
        line = file.readline()

    line = file.readline()

file.close()

export_csv(list)

