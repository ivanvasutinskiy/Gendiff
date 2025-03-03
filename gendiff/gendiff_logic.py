import json
import os

from gendiff.get_difference import get_difference


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    diff = get_difference(data1, data2)
    return diff


def parse_data(data, format_name):
    if format_name == 'json':
        return json.loads(data)


def load_file(file_path):
    with open(os.path.abspath(f'tests/fixtures/{file_path}')) as file:
        extension = file_path.split('.')[-1]
        if extension == 'json':
            data_object = json.load(file)
            data = json.dumps(data_object, sort_keys=True, indent=4)
            print()
            return parse_data(data, extension)

