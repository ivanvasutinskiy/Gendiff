def transform_changes(changes):
    def process_node(item):
        if item['action'] == 'added':
            return {f"+ {item['name']}": item['new_value']}
        elif item['action'] == 'deleted':
            return {f"- {item['name']}": item['old_value']}
        elif item['action'] == 'modified':
            return {f"- {item['name']}": item['old_value'],f"+ {item['name']}": item['new_value']}
        elif item['action'] == 'unchanged':
            return {f"  {item['name']}": item['value']}
        elif item['action'] == 'nested':
            nested_result = {}
            for child in item['children']:
                nested_result.update(process_node(child))
            return {f"  {item['name']}": nested_result}

    result = {}
    for item in changes:
        result.update(process_node(item))

    return result