def get_difference(dict1, dict2):
    differences = '{\n'

    for key in dict1:
        if key not in dict2:
            differences += f'  - {key}: {str(dict1[key]).lower()}\n'
        elif dict1[key] != dict2[key]:
            differences += f'  - {key}: {str(dict1[key]).lower()}\n'
            differences += f'  + {key}: {str(dict2[key]).lower()}\n'
        else:
            differences += f'    {key}: {str(dict1[key]).lower()}\n'

    for key in dict2:
        if key not in dict1:
            differences += f'  + {key}: {str(dict2[key]).lower()}\n'
    differences += '}'
    return differences