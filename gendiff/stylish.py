from gendiff.generate import get_difference

def transform_changes(changes):
    def process_node(item, depth):
        indent = '..' * depth  # Уровень отступа
        if item['action'] == 'added':
            return f"{indent}+ {item['name']}: {to_str(item['new_value'])}\n"
        elif item['action'] == 'deleted':
            return f"{indent}- {item['name']}: {to_str(item['old_value'])}\n"
        elif item['action'] == 'modified':
            return f"{indent}- {item['name']}: {to_str(item['old_value'])}\n" + \
            f"..{indent}+ {item['name']}: {to_str(item['new_value'])}\n"
        elif item['action'] == 'unchanged':
            return f"{indent}  {item['name']}: {to_str(item['value'])}\n"
        elif item['action'] == 'nested':
            nested_result = f"{indent}  {item['name']}: {{\n"
            for child in item['children']:
                nested_result += f"{indent}{process_node(child, depth + 1)}"
            nested_result += f"{indent}  }}\n"
            return nested_result

    result = ['{']
    for item in changes:
        result.append(process_node(item, 1))
    return '\n'.join(result) + '\n}'


def to_str(value):
    if isinstance(value, dict):
        return transform_changes(get_difference(value, value))
    if value is False:
        return "false"
    if value is True:
        return "true"
    if value is None:
        return "null"
    if value == 0:
        return "0"
    else:
        return value