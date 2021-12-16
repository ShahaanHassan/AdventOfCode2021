import copy
import time
from math import inf
from operator import attrgetter

import numpy as np

from helpers.file_manager import read_file_as_list


class Node:

    def __init__(self, risk: int, y: int, x: int, dist=inf):
        self.risk = risk
        self.y = y
        self.x = x
        self.dist = dist

    # for debugging
    def __repr__(self):
        return str((self.risk, self.dist))

    def __add__(self, other):
        new_risk = self.risk + other
        self.risk = 1 if new_risk > 9 else new_risk
        return self


def grid_size(grid):
    return len(grid[0]), len(grid)


def bound(val: int, limit: int) -> int:
    return 0 <= val < limit


def find_neighbours(grid, node, visited):
    y, x = node.y, node.x
    width, height = grid_size(grid)
    return [grid[yy][xx] for yy, xx in zip([y, y, y - 1, y + 1], [x - 1, x + 1, x, x])
            if bound(yy, height) and bound(xx, width) and grid[yy][xx] not in visited]


def refresh_nodes(grid):
    for y, line in enumerate(grid):
        for x, risk in enumerate(line):
            old_node = grid[y][x]
            grid[y][x] = Node(old_node.risk, y, x, old_node.dist)


def process_input(data: list):
    width, height = grid_size(data)
    grid = np.empty((height, width), dtype=Node)
    for y, line in enumerate(data):
        for x, risk in enumerate(line):
            grid[y][x] = Node(int(risk), y, x)
    grid[0][0].dist = 0
    grid[0][0].risk = 0
    return grid


def process_bigger_input(data: list):
    width, height = grid_size(data)
    initial_grid = np.empty((height, width), dtype=Node)
    for y, line in enumerate(data):
        for x, risk in enumerate(line):
            initial_grid[y][x] = Node(int(risk), y, x)
    row_grid = copy.deepcopy(initial_grid)

    for j in range(1, 5):
        initial_grid += 1
        row_grid = np.concatenate((row_grid, copy.deepcopy(initial_grid)), axis=1)
        print()

    final_grid = copy.deepcopy(row_grid)
    for k in range(1, 5):
        row_grid += 1
        final_grid = np.concatenate((final_grid, copy.deepcopy(row_grid)))
    final_grid[0][0].dist = 0
    final_grid[0][0].risk = 0
    refresh_nodes(final_grid)
    return final_grid


def find_paths(grid, queue: set, visited: set, goal: Node):
    while True:
        current = min(queue, key=attrgetter('dist'))
        queue.remove(current)
        neighbours = find_neighbours(grid, current, visited)
        if goal in visited or len(queue) == 0:
            return goal
        for n in neighbours:
            if n not in visited:
                calc_dist = current.dist + n.risk
                if calc_dist < n.dist:
                    n.dist = calc_dist
        visited.add(current)


def start_search(grid):
    queue = {p for line in grid for p in line}
    node = find_paths(grid, queue, set(), grid[-1][-1])
    return node.dist


def part_1(data: list) -> int:
    grid = process_input(data)
    return start_search(grid)


def part_2(data: list) -> int:
    grid = process_bigger_input(data)
    return start_search(grid)


if __name__ == '__main__':
    start = time.time() * 1000
    input_data = read_file_as_list('day15/input.txt')
    print(part_1(input_data))
    print(part_2(input_data))
    end = time.time() * 1000
    # Takes roughly 52 minutes for part b
    print('time taken: {} ms'.format(round(end - start, 2)))
