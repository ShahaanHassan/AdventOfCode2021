from helpers.file_manager import read_file_as_int_list


def get_number_of_higher_readings(input_data: list) -> int:
    higher_readings = 0
    for index, reading in enumerate(input_data):
        if index > 0:
            if reading > input_data[index - 1]:
                higher_readings += 1
    return higher_readings


def part_1(input_data: list) -> int:
    return get_number_of_higher_readings(input_data)


def part_2(input_data: list) -> int:
    window = 3
    return get_number_of_higher_readings([sum(input_data[i:i+window]) for i in range(0, len(input_data))])


input_dir = 'day1/input.txt'
data = read_file_as_int_list(input_dir)
print(part_1(data))
print(part_2(data))