from dataclasses import dataclass


@dataclass
class Record:
    state: str
    gender: str
    year: int
    name: str
    count: int


def read_file(file_directory):

    # Read and split
    with open(file_directory, "r") as f:
        data = [line.strip().split(",") for line in f]

    # Convert to list of records
    records = []
    for datum in data:
        temp = Record(datum[0], datum[1], int(datum[2]), datum[3], int(datum[4]))
        records.append(temp)

    # Return list of records
    return records


def build_dictionary(records):
    name_occurance = {}
    for record in records:
        _name = record.name
        _count = record.count
        if _name not in name_occurance:
            name_occurance[_name] = 0
        name_occurance[_name] += _count

    return name_occurance


def main():
    records = read_file("ny.txt")
    names = build_dictionary(records)

    print(f"There are {len(names)} unique names!")

    input_name = input("Enter a name to search for: ")
    try:
        print(f"{input_name} appeared {names[input_name]} times)")
    except KeyError:
        print(f"{input_name} not found!")


if __name__ == "__main__":
    main()
