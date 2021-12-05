import re
from typing import Tuple

import numpy as np

from helpers.file_manager import read_file_as_list


def format_input(input_data: list) -> list:
    return list(map(lambda x: list(((int(t[0]), int(t[1])) for t in x)),
                    [re.findall('(\d*),(\d*)', line) for line in input_data]))


def get_coords(line: list) -> Tuple[int, int, int, int]:
    point_a, point_b = line
    return point_a[0], point_b[0], point_a[1], point_b[1]


def get_range(p1: int, p2: int) -> range:
    return range(p1, p2 + 1) if p1 < p2 else range(p1, p2 - 1, -1)


# ndarray is [row][column] so points are flipped to [y][x]
def create_grid(lines: list, diagonals=False, size=1000):
    grid = np.zeros([size, size])
    for line in lines:
        x1, x2, y1, y2 = get_coords(line)
        if x1 == x2:
            for y in get_range(y1, y2):
                grid[y][x1] += 1
        elif y1 == y2:
            for x in get_range(x1, x2):
                grid[y1][x] += 1
        elif diagonals:
            for x, y in zip(get_range(x1, x2), get_range(y1, y2)):
                grid[y][x] += 1

    return grid


def count_overlaps(grid) -> int:
    return sum(x > 1 for line in grid for x in line)


def part_1(input_data: list):
    lines = format_input(input_data)
    return count_overlaps(create_grid(lines, False))


def part_2(input_data: list):
    lines = format_input(input_data)
    return count_overlaps(create_grid(lines, True))


if __name__ == "__main__":
    data = read_file_as_list('day5/input.txt')
    print(part_1(data))
    print(part_2(data))
