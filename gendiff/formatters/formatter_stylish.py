from gendiff.generate import get_difference

SPACES_PER_LEVEL = 4
SHIFT_LEFT = 2


def stylish(dict_diff: dict):
    return make_string(dict_diff)


def make_string(tree, depth=1):
    def walk(node, depth, result=""):
        for item in node:
            new_depth = depth + 1
            indent = make_indent(depth)
            result += "\n"
            if item['action'] == 'removed':
                result += f"{indent}- {item['name']}: " \
                f"{str(to_str(item['value'], new_depth))}"
            elif item['action'] == 'added':
                result += f"{indent}+ {item['name']}: " \
                f"{str(to_str(item['value'], new_depth))}"
            elif item['action'] == 'nested':
                result += f"{indent}  {item['name']}: " \
                f"{walk(item['children'], new_depth, result="")}"
            elif item['action'] == 'updated':
                result += f"{indent}- {item['name']}: " \
                f"{str(to_str(item['old_value'], new_depth))}\n"
                result += f"{indent}+ {item['name']}: " \
                f"{str(to_str(item['new_value'], new_depth))}"
            elif item['action'] == 'unchanged':
                result += f"{indent}  {item['name']}: " \
                f"{str(to_str(item['value'], new_depth))}"
      
        return "{" + f"{result}\n{SPACES_PER_LEVEL * (depth - 1) * " " + '}'}"
    return walk(tree, depth, "")


def to_str(value, depth=0):
    if isinstance(value, dict):
        return make_string(get_difference(value, value), depth)
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


def make_indent(depth):
    indent = (depth * SPACES_PER_LEVEL - SHIFT_LEFT) * " "
    return indent