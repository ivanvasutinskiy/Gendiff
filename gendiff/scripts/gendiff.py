from gendiff.gendiff_logic import generate_diff
from gendiff.parser import description_of_thegender_spread


def main():
    args = description_of_thegender_spread()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)

if __name__ == "__main__":
    main()