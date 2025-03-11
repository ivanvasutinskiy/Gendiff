import json
import yaml
from yaml.loader import SafeLoader

def parse(data, format_name):
    if format_name == 'json':
        return json.loads(data)
    if format_name == 'yaml' or 'yml':
        return yaml.load(data, Loader=SafeLoader)