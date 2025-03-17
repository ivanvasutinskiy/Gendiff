import json
import yaml


def load_file(path_to_file):
    data = open(path_to_file)
    extension = path_to_file.split(".")[-1]
    return data, extension


def parse(data, extension):
    if extension == "yml" or extension == "yaml":
        return yaml.safe_load(data)
    if extension == "json":
        return json.load(data)