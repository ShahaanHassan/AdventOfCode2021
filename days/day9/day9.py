from collections import namedtuple

import numpy as np

from helpers.file_manager import read_file_as_list

Point = namedtuple('point', 'val y x')


class Node:

    def __init__(self, point: Point):
        self.point = point
        self.neighbours = []

    def __eq__(self, other):
        return self.point == other.point

    def add_neighbour(self, val):
        self.neighbours.append(val)


def format_data(input_data: list):
    return np.array([[int(x) for x in line] for line in input_data])


def out_of_bounds(grid, y, x) -> bool:
    y_range, x_range = grid.shape
    return y >= y_range or x >= x_range or y < 0 or x < 0


def check_adjacent(grid, val, y, x) -> bool:
    return out_of_bounds(grid, y, x) or grid[y][x] > val


def add_nodes(grid, node):
    val, y, x = node.point
    for yy, xx in zip([y, y, y - 1, y + 1], [x - 1, x + 1, x, x]):
        if not out_of_bounds(grid, yy, xx) and 9 > grid[yy][xx] > val:
            node.add_neighbour(Node(Point(grid[yy][xx], yy, xx)))


def get_centers(grid) -> list:
    low_values = []
    for y, line in enumerate(grid):
        for x, i in enumerate(line):
            results = []
            for yy, xx in zip([y, y, y - 1, y + 1], [x - 1, x + 1, x, x]):
                results.append(check_adjacent(grid, i, yy, xx))
            if all(results):
                low_values.append(Point(i, y, x))
    return low_values


def chart_crater(grid, start_node: Node):
    queue = [start_node]
    visited = []
    basin_size = 0

    while queue:
        node_to_check = queue.pop(0)
        if node_to_check not in visited:
            basin_size += 1
            visited.append(node_to_check)
            add_nodes(grid, node_to_check)
            queue += node_to_check.neighbours
    return basin_size


def part_1(input_data):
    grid = format_data(input_data)
    return sum(x.val+1 for x in get_centers(grid))


def part_2(input_data):
    grid = format_data(input_data)
    centers = get_centers(grid)
    biggest_craters = [0] * 3
    for point in centers:
        start_node = Node(point)
        size = chart_crater(grid, start_node)
        smallest_crater = min(biggest_craters)
        if size > smallest_crater:
            biggest_craters[biggest_craters.index(smallest_crater)] = size
    return np.prod(biggest_craters)


if __name__ == "__main__":
    data = read_file_as_list('day9/input.txt')
    print(part_1(format_data(data)))
    print(part_2(format_data(data)))
