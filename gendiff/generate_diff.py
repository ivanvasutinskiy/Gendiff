

from gendiff.formatters.form_selector import select_formatter
from gendiff.generate import get_difference
from gendiff.parser import load_file, parse


def generate_diff(path_to_file1, path_to_file2, format_name="stylish"):
    dict1 = parse(*load_file(path_to_file1))
    dict2 = parse(*load_file(path_to_file2))
    dict_diff = get_difference(dict1, dict2)
    return select_formatter(dict_diff, format_name)



