from gendiff.gendiff_logic import generate_diff
from gendiff.cli import description_of_thegender_spread

def main():
    args = description_of_thegender_spread()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    with open('output.txt', 'w') as file:
        file.write(diff)
    print(diff)


if __name__ == "__main__":
    main()