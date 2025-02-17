import argparse
import json
import os

def description_of_thegender_spread():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    my_namespace = parser.parse_args()
    print(my_namespace.FORMAT)

def first_file():
    with open(os.path.abspath('gendiff/file1.json')) as json_file:
        data = json.load(json_file)
        data1 = json.dumps(data, sort_keys=True, indent=4)
        print(data1)

def second_file():
    with open(os.path.abspath('gendiff/file2.json')) as json_file:
        data = json.load(json_file)
        data2 = json.dumps(data, sort_keys=True, indent=4)
        print(data2)