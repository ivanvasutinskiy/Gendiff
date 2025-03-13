import json
import os
import yaml
import re
import pprint
from gendiff.parser import parse
from yaml.loader import SafeLoader
from gendiff.generate import get_difference
from gendiff.stylish import transform_changes


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    diff = get_difference(data1, data2)
    print(diff)
    return transform_changes(diff)


def load_file(file_path):
    with open(os.path.abspath(f'tests/fixtures/{file_path}')) as file:
        extension = file_path.split('.')[-1]
        if extension == 'json':
            data_object = json.load(file)
            data = json.dumps(data_object, sort_keys=True, indent=4)
            return parse(data, extension)
        if extension == 'yaml' or 'yml':
            data_object = yaml.load(file, Loader=SafeLoader)
            data = yaml.dump(data_object, indent=4)
            return parse(data, extension)


