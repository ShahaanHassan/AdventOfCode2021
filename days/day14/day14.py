from collections import defaultdict
from typing import Tuple

from helpers.file_manager import read_file_as_list
import time


def process_input(data: list) -> Tuple[list, dict]:
    base = data[0]
    pairs = {x: y for x, y in (line.split(' -> ') for line in data[2:])}
    return base, pairs


def apply_poly(poly_pairs: dict, pairs: dict) -> dict:
    new_pairs = defaultdict(int)
    for pair, count in poly_pairs.items():
        if pair in pairs:
            new_pairs[pair[0] + pairs[pair]] += count
            new_pairs[pairs[pair] + pair[1]] += count
    return new_pairs


def chain_polys(data: list, iterations: int) -> int:
    base, pairs = process_input(data)
    poly_pairs = defaultdict(int)

    for x in range(len(base)):
        poly_pairs[base[x:x + 2]] += 1

    for _ in range(iterations):
        poly_pairs = apply_poly(poly_pairs, pairs)

    sums = defaultdict(int)
    for x, y in poly_pairs.items():
        sums[x[0]] += y
    sums[base[-1]] += 1
    return max(sums.values()) - min(sums.values())


def part_1(data: list) -> int:
    return chain_polys(data, 10)


def part_2(data: list) -> int:
    return chain_polys(data, 40)


if __name__ == '__main__':
    input_data = read_file_as_list('day14/input.txt')
    start = time.time() * 1000
    print(part_1(input_data))
    print(part_2(input_data))
    end = time.time() * 1000
    # both parts roughly take between 3-4 ms.
    print('time taken: {} ms'.format(round(end-start, 2)))
