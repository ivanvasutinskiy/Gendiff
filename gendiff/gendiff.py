import argparse

def description_of_thegender_spread():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    my_namespace = parser.parse_args()
    print(my_namespace.FORMAT)