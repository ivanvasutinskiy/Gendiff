from gendiff.formatters.formatter_json import to_json
from gendiff.formatters.formatter_plain import plain
from gendiff.formatters.formatter_stylish import stylish


def select_formatter(dict, format_name):
    match format_name:
        case 'stylish':
            return stylish(dict)
        case 'plain':
            return plain(dict)
        case 'json':
            return to_json(dict)
    