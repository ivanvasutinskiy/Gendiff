import json

import yaml
from yaml.loader import SafeLoader


def parse(data, format_name):
    if format_name == 'json':
        return data
    if format_name == 'yaml' or 'yml':
        return data
    

