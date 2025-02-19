import argparse
import json
import os

from gendiff.generate_diff import compare_dictionaries


def description_of_thegender_spread():
    parser = argparse.ArgumentParser(description='''
        Compares two configuration files and shows a difference.''')
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    dict1 = json.loads(first_f(args.first_file))
    dict2 = json.loads(second_f(args.second_file))
    diff = (compare_dictionaries(dict1, dict2))
    print(diff)


def first_f(file1):
    with open(os.path.abspath(f'gendiff/{file1}')) as json_file:
        data = json.load(json_file)
        data1 = json.dumps(data, sort_keys=True, indent=4)
        return data1


def second_f(file2):
    with open(os.path.abspath(f'gendiff/{file2}')) as json_file:
        data = json.load(json_file)
        data2 = json.dumps(data, sort_keys=True, indent=4)
        return data2