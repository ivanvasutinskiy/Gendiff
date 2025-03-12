def transform_changes(changes):
    def process_node(item, depth):
        indent = '..' * depth  # Уровень отступа
        if item['action'] == 'added':
            return f"{indent}+ {item['name']}: {item['new_value']}\n"
        elif item['action'] == 'deleted':
            return f"{indent}- {item['name']}: {item['old_value']}\n"
        elif item['action'] == 'modified':
            return f"{indent}- {item['name']}: {item['old_value']}\n" + \
            f"..{indent}+ {item['name']}: {item['new_value']}\n"
        elif item['action'] == 'unchanged':
            return f"{indent}  {item['name']}: {item['value']}\n"
        elif item['action'] == 'nested':
            nested_result = f"{indent}  {item['name']}: {{\n"
            for child in item['children']:
                nested_result += f"{indent}{process_node(child, depth + 1)}"
            nested_result += f"{indent}  }}\n"
            return nested_result

    result = ['{']
    for item in changes:
        result.append(process_node(item, 1).strip())
    return '\n'.join(result)