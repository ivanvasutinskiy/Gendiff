import os
import json
from gendiff.gendiff import description_of_thegender_spread

def main():
    description_of_thegender_spread()


if __name__ == "__main__":
    main()

def first_file():
    with open(os.path.abspath('gendiff/file1.json')) as json_file:
        data = json.load(json_file)
        data1 = json.dumps(data, sort_keys=True, indent=4)
        print(data1)

if __name__ == "__firs_file__":
    firs_file()

def second_file():
    with open(os.path.abspath('gendiff/file2.json')) as json_file:
        data = json.load(json_file)
        data2 = json.dumps(data, sort_keys=True, indent=4)
        print(data2)
    
if __name__ == "__second_file__":
    second_file()