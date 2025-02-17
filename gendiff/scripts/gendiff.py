import os
import json
from gendiff.gendiff import description_of_thegender_spread

def main():
    description_of_thegender_spread()


if __name__ == "__main__":
    main()

def get_gendiff():
    with open(os.path.abspath('gendiff/file1.json')) as json_file:
        data = json.load(json_file)
        data1 = json.dumps(data, sort_keys=True, indent=4)
        print(data1)
    with open(os.path.abspath('gendiff/file2.json')) as json_file:
        data = json.load(json_file)
        data2 = json.dumps(data, sort_keys=True, indent=4)
        print(data2)
    
if __name__ == "__get_gendiff__":
    get_gendiff()