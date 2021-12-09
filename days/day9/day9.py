from helpers.file_manager import read_file_as_list

import numpy as np


def format_data(input_data: list):
    return np.array([[x for x in line] for line in input_data])


def check_bounds(grid, x, y) -> bool:
    x_range, y_range = grid.shape
    return y >= y_range or x >= x_range or y < 0 or x < 0


def check_adjacent(grid, val, y, x) -> bool:
    return check_bounds(grid, x, y) or grid[y][x] > val


def part_1(input_data) -> int:
    low_values = []
    for y, line in enumerate(input_data):
        for x, i in enumerate(line):
            results = []
            for yy, xx in zip([y, y, y-1, y+1], [x-1, x+1, x, x]):
                results.append(check_adjacent(input_data, i, yy, xx))
            if all(results):
                low_values.append(i)
    return sum(int(x)+1 for x in low_values)


if __name__ == "__main__":
    data = read_file_as_list('day9/input.txt')
    print(part_1(format_data(data)))
