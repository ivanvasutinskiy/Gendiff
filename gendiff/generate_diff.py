import json
import os

import yaml
from yaml.loader import SafeLoader

from gendiff.formatters.form_selector import select_formatter
from gendiff.generate import get_difference
from gendiff.parser import parse


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    dict_diff = get_difference(data1, data2)
    return select_formatter(dict_diff, format_name)

def load_file(file_path):
    for root, dirs, files in os.walk('/'):
        if file_path in files:
            file_path = os.path.join(root, file_path)
            with open(os.path.abspath(file_path), 'r') as file:
                extension = file_path.split('.')[-1]
                if extension == 'json':
                    data_object = json.load(file)
                    data = json.dumps(data_object, sort_keys=True, indent=4)
                    return parse(data, extension) 
                if extension == 'yaml' or  extension == 'yml':
                    data_object = yaml.load(file, Loader=SafeLoader)
                    data = yaml.dump(data_object, indent=4)
                    return parse(data, extension)


