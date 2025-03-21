import pytest

from gendiff.generate_diff import generate_diff


@pytest.fixture
def file_one():
    return open('./tests/fixtures/file1_for_tests.txt')


@pytest.fixture
def file_two():
    return open('./tests/fixtures/file2_for_tests.txt')


@pytest.fixture
def difference():
    with open('./tests/fixtures/result_stylish.txt') as file:
        return file.read()


def test_generate_diff_json(difference):
    result = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json')
    assert result.strip() == difference.strip()


def test_generate_diff_yaml(difference):
    result = generate_diff('./tests/fixtures/file1.yaml',
                           './tests/fixtures/file2.yaml')
    assert result.strip() == difference.strip()


def test_generate_diff_yml(difference):
    result = generate_diff('./tests/fixtures/file1.yml',
                           './tests/fixtures/file2.yml')
    assert result.strip() == difference.strip()


def test_generate_diff_json_and_yaml(difference):
    result = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.yaml')
    assert result.strip() == difference.strip()


def test_generate_diff_json_and_yml(difference):
    result = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.yml')
    assert result.strip() == difference.strip()    



