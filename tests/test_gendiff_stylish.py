import pytest

from gendiff.generate_diff import generate_diff

@pytest.fixture


def file_one():
    return {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}

@pytest.fixture


def file_two():
    return {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}

@pytest.fixture


def difference():
    return """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

def test_generate_diff(difference):
    result = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json')
    assert result.strip() == difference.strip()

def test_generate_diff(difference):
    result = generate_diff('./tests/fixtures/file1.yaml',
                           './tests/fixtures/file2.yaml')
    assert result.strip() == difference.strip()

def test_generate_diff(difference):
    result = generate_diff('./tests/fixtures/file1.yml',
                           './tests/fixtures/file2.yml')
    assert result.strip() == difference.strip()


    