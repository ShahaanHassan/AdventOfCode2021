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
    sliding_window_sums = []
    window = 3

    for i in range(0, len(input_data)):
        sliding_window_sums.append(sum(input_data[i:i+window]))

    return get_number_of_higher_readings(sliding_window_sums)


input_dir = 'day1/input'
data = read_file_as_int_list(input_dir)
print(part_1(data))
print(part_2(data))