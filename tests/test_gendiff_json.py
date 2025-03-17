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
    return """[
  {
    "action": "nested",
    "name": "common",
    "children": [
      {
        "action": "added",
        "name": "follow",
        "value": false
      },
      {
        "action": "unchanged",
        "name": "setting1",
        "value": "Value 1"
      },
      {
        "action": "removed",
        "name": "setting2",
        "value": 200
      },
      {
        "action": "updated",
        "name": "setting3",
        "new_value": null,
        "old_value": true
      },
      {
        "action": "added",
        "name": "setting4",
        "value": "blah blah"
      },
      {
        "action": "added",
        "name": "setting5",
        "value": {
          "key5": "value5"
        }
      },
      {
        "action": "nested",
        "name": "setting6",
        "children": [
          {
            "action": "nested",
            "name": "doge",
            "children": [
              {
                "action": "updated",
                "name": "wow",
                "new_value": "so much",
                "old_value": ""
              }
            ]
          },
          {
            "action": "unchanged",
            "name": "key",
            "value": "value"
          },
          {
            "action": "added",
            "name": "ops",
            "value": "vops"
          }
        ]
      }
    ]
  },
  {
    "action": "nested",
    "name": "group1",
    "children": [
      {
        "action": "updated",
        "name": "baz",
        "new_value": "bars",
        "old_value": "bas"
      },
      {
        "action": "unchanged",
        "name": "foo",
        "value": "bar"
      },
      {
        "action": "updated",
        "name": "nest",
        "new_value": "str",
        "old_value": {
          "key": "value"
        }
      }
    ]
  },
  {
    "action": "removed",
    "name": "group2",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  {
    "action": "added",
    "name": "group3",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
]"""

def test_generate_diff(difference):
    result = generate_diff('./tests/fixtures/file1.json', \
                            './tests/fixtures/file2.json', 'json')
    assert result.strip() == difference.strip()

def test_generate_diff(difference):
    result = generate_diff('./tests/fixtures/file1.yaml', \
                            './tests/fixtures/file2.yaml', 'json')
    assert result.strip() == difference.strip()

def test_generate_diff(difference):
    result = generate_diff('./tests/fixtures/file1.yml', \ 
                           './tests/fixtures/file2.yml', 'json')
    assert result.strip() == difference.strip()