
def plain(dict):
    return make_string(add_path(dict))


def add_path(tree):
    def walk(nod, path, new_tree=[]):
        for child in nod:
            new_path = f"{path}{child['name']}."
            child.update({"path": path})
            new_tree.append(child)
            if 'children' in child:
                walk(child.get('children'), new_path)
        return new_tree

    return walk(tree, '')


def make_string(node):
    result = []
    for child in node:
        property = f"{child['path']}{child['name']}"
        action = child['action']
        if action != 'nested' and action != 'unchanged':
            string = f"Property '{property}' was {action}"
            if action == 'added':
                string += f" with value: {to_str(child['value'])}"
            if action == 'updated':
                string += f". From {to_str(child['old_value'])} " \
                f"to {to_str(child['new_value'])}"
            result.append(string)
    return "\n".join(result)
    

def to_str(value):
    if value is False:
        return "false"
    if value is True:
        return "true"
    if value is None:
        return "null"
    if value == 0:
        return "0"
    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"   