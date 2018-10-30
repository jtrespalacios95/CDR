import pandas as pd
import json
from datetime import datetime


file = open("baf_test.txt")
line = file.readline()
head = False
body = False
row = False
row_obj = {}
list = []
listKey = []
specialField = ['Sensor']

def get_name(line):
    var = line.split(':')[0]
    return var.replace("'", '')

def get_value(line):
    var = line.split(':',1)[1]
    return var.replace(',', '')

def  get_value_object (line):
    if line.split(':')[0] in specialField:
        pass



def insert(key,value):
    if key is not None:
        if key not in row_obj.keys():
            row_obj[key] = value.strip()
        else:
            row_obj[key] = row_obj[key] + ", " + value.strip()


def export_csv (list):
    aux = json.dumps(list)
    df = pd.read_json(aux)
    name = datetime.now().strftime('%Y%m%d%H%M%S')

    df.to_csv('csv/BAF-'+name+'.csv', index=False, sep='|')

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
        list.append(row_obj)
        keys = row_obj.keys()
        row_obj = {}

    if 'File end' in line:
        head = True
        body = False
        line = file.readline()

    line = file.readline()

file.close()

export_csv(list)
