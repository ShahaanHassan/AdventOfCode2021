from helpers.file_manager import read_lines_with_split_as_int


def get_fuel_with_sum(diff: int) -> int:
    return diff * (diff + 1) // 2


def part_1(input_data: list) -> int:
    return min([sum([abs(x-i) for x in input_data]) for i in range(min(input_data), max(input_data))])


def part_2(input_data: list) -> int:
    return min([sum([get_fuel_with_sum(abs(x-i)) for x in input_data]) for i in range(min(input_data), max(input_data))])


if __name__ == "__main__":
    data = read_lines_with_split_as_int('day7/input.txt')
    print(part_1(data))
    print(part_2(data))
