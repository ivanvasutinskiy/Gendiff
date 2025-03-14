from gendiff.formatters.formatter_json import to_json
from gendiff.formatters.formatter_plain import plain
from gendiff.formatters.formatter_stylish import stylish


def select_formatter(dict, format_name):
    if format_name == 'stylish':
        return stylish(dict)
    if format_name == 'plain':
        return plain(dict)
    if format_name == 'json':
        return to_json(dict)
    