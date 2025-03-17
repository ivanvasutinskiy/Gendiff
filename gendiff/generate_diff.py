import json
import os

import yaml
from yaml.loader import SafeLoader

from gendiff.formatters.form_selector import select_formatter
from gendiff.generate import get_difference



def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    if data1 != None and data2 != None:
        dict_diff = get_difference(data1, data2)
        return select_formatter(dict_diff, format_name)
    

def load_file(file_path):
    for root, dirs, files in os.walk('/'):
        if file_path in files:
            file_path = os.path.join(root, file_path)
            try:
                with open(os.path.abspath(file_path), 'r') as file:
                    extension = file_path.split('.')[-1]
                    if extension == 'json':
                        data = json.load(file)
                        return data
                    elif extension == 'yaml' or  extension == 'yml':
                        data = yaml.safe_load(file)
                        return data
                    else:
                        print(f"Неподдерживаемый формат файла: {extension}")
                        return None
            except FileNotFoundError:
                print(f"Файл не найден: {file_path}")
                return None
            except json.JSONDecodeError:
                print(f"Ошибка декодирования JSON в файле: {file_path}")
                return None
            except yaml.YAMLError as e:
                print(f"Ошибка при загрузке YAML из файла: {file_path} - {e}")
                return None
    print(f"Файл с именем {file_path} не найден в корневой директории или ее поддиректориях.")
    return None



