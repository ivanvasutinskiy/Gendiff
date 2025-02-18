def compare_dictionaries(dict1, dict2):
    differences = {}

    for key in dict1:
        if key not in dict2:
            differences[f'- {key}'] = dict1[key]
        elif dict1[key] != dict2[key]:
            differences[f'- {key}'] = dict1[key]
            differences[f'+ {key}'] = dict2[key]
        else:
            differences[key] = dict1[key]

    for key in dict2:
        if key not in dict1:
            differences[f'+ {key}'] =  dict2[key]

    return differences