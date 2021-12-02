from helpers.file_manager import read_file_as_list


def part_1(input_data: list) -> int:
    horizontal, depth = 0, 0
    for line in input_data:
        command, distance = line.split(' ')
        distance = int(distance)
        if command == 'forward':
            horizontal += distance
        elif command == 'down':
            depth += distance
        elif command == 'up':
            depth -= distance
    return depth * horizontal


def part_2(input_data: list) -> int:
    horizontal, depth, aim = 0, 0, 0

    for line in input_data:
        command, distance = line.split(' ')
        distance = int(distance)
        if command == 'forward':
            horizontal += distance
            depth += distance * aim
        elif command == 'down':
            aim += distance
        elif command == 'up':
            aim -= distance
    return depth * horizontal


input_dir = 'day2/input.txt'
data = read_file_as_list(input_dir)
print(part_1(data))
print(part_2(data))
