from helpers.file_manager import read_file_as_list


# First iteration of part 1 which works but doesn't extend well for part 2
def old_part_1(input_data: list) -> int:
    binary_sums = {index: 0 for index in range(0, len(input_data[0]))}
    gamma, epsilon = '', ''
    total_lines = len(input_data)

    for line in input_data:
        for index, bit in enumerate(line):
            binary_sums.update({index: binary_sums[index] + int(bit)})

    for key, value in binary_sums.items():
        if value >= total_lines / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def most_common(input_data: list, index: int, dominant: bool) -> str:
    total_ones = 0
    for line in input_data:
        total_ones += int(line[index])
    if total_ones >= len(input_data) / 2:
        if dominant:
            return '1'
        else:
            return '0'
    else:
        if dominant:
            return '0'
        else:
            return '1'


def true_reading(input_data: list, dominant: bool) -> str:
    oxygen_data = input_data.copy()
    for i in range(0, len(input_data[0])):
        most_common_value = most_common(oxygen_data, i, dominant)
        oxygen_data = [x for x in oxygen_data if x[i] == most_common_value]
        if len(oxygen_data) == 1:
            return oxygen_data[0]
    return ''


def part_1(input_data: list) -> int:
    gamma, epsilon = '', ''
    for i in range(0, len(input_data[0])):
        gamma += most_common(input_data, i, True)
        epsilon += most_common(input_data, i, False)
    return int(gamma, 2) * int(epsilon, 2)


def part_2(input_data: list) -> int:
    oxygen, carbon = true_reading(input_data, True), true_reading(input_data, False)
    return int(oxygen, 2) * int(carbon, 2)


data = read_file_as_list('day3/input.txt')
print(part_1(data))
print(part_2(data))
