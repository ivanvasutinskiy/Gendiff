from gendiff.generate_diff import compare_dictionaries

def test_extract_links():
    with_links_path = 'gendiff/file1.json'
    with open(with_links_path) as f:
        file = f.read()
        






def test_compare_dictionaries():
    dict_a = {
        'apple': 1,
        'banana': 2,
        'cherry': 3
    }

    dict_b = {
        'banana': 2,
        'cherry': 4,
        'date': 5
    }

    expected_differences = [
        "- apple: 1",
        "- cherry: 3 (в первом словаре) <> + cherry: 4 (во втором словаре)",
        "+ date: 5"
    ]


    