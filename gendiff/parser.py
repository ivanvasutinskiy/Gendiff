import json

import yaml


def load_file(path_to_file):
    data = open(path_to_file)
    extension = path_to_file.split(".")[-1]
    return data, extension


def parse(data, format_name):
    match format_name:
        case 'json':
            return json.load(data)
        case 'yml' | 'yaml':
            return yaml.safe_load(data)
        case _:
            raise ValueError("Unsupported data format")
    
    
    