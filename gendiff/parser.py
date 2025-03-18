import json

import yaml


def load_file(path_to_file):
    data = open(path_to_file)
    extension = path_to_file.split(".")[-1]
    return data, extension


def parse(data, format_name):
    if format_name == 'json':
        return json.load(data)
    if format_name == 'yaml' or format_name == 'yml':
        return yaml.safe_load(data)
    raise ValueError("Unsupported data format")
    
    
    