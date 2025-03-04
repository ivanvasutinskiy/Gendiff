import pytest

from gendiff.gendiff_logic import generate_diff

@pytest.fixture
def file_one():
    return {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    }

@pytest.fixture
def file_two():
    return {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
    }

@pytest.fixture
def difference():
    return """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

def test_generate_diff(file_one, file_two, difference):
    result = generate_diff('file1.yaml', 'file2.yaml')
    assert result.strip() == difference.strip()
