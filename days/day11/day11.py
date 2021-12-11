import numpy as np

from helpers.file_manager import read_file_as_list


class Point:
    def __init__(self, val: int, y: int, x: int):
        self.val = val
        self.y = y
        self.x = x

    def __repr__(self):
        return str(self.val)

    def __add__(self, other):
        self.val += other
        return self


def format_data(input_data: list, size=10):
    grid = np.array([[int(x) for x in line] for line in input_data])
    p_grid = np.zeros([size, size], Point)
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            p_grid[y][x] = Point(val, y, x)
    return p_grid


def bound(val: int, size=10) -> int:
    if val > size:
        return size
    if val < 0:
        return 0
    return val


def flash_octopuses(grid, steps=100, size=10, convergence=False) -> int:
    final_sum = 0
    for step in range(0, steps):
        have_flashed, to_flash = set(), set()
        grid += np.ones([size, size], np.int8)
        for line in grid:
            for p in line:
                if p.val > 9:
                    to_flash.add(p)
        flash_count = 0
        while to_flash:
            tf = to_flash.pop()
            flash_count += 1
            for y in range(bound(tf.y - 1), bound(tf.y + 2)):
                for x in range(bound(tf.x - 1), bound(tf.x + 2)):
                    cp = grid[y][x]
                    if not cp == tf and cp not in have_flashed:
                        cp.val += 1
                        if cp.val > 9:
                            to_flash.add(cp)
            have_flashed.add(tf)
            for fp in have_flashed:
                fp.val = 0

        final_sum += flash_count
        if convergence and flash_count == size*size:
            return step + 1

    return final_sum


def part_1(grid) -> int:
    return flash_octopuses(grid)


def part_2(grid) -> int:
    return flash_octopuses(grid, 10000, convergence=True)


if __name__ == "__main__":
    data = read_file_as_list('day11/input.txt')
    print(part_1(format_data(data)))
    print(part_2(format_data(data)))
