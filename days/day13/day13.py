import numpy as np

from helpers.file_manager import read_file_as_list


class Mark(str):

    def __add__(self, other):
        if other == '#':
            return Mark('#')
        else:
            return self


def format_data(data: list):
    points, instructions = [], []
    for index, line in enumerate(data):
        if line == '':
            points, instructions = data[:index], data[index + 1:]
            break
    width = max(int(x) for x, _ in (line.split(',') for line in points))
    height = max(int(y) for _, y in (line.split(',') for line in points))
    page = np.array([[Mark('.') for _ in range(width + 1)] for _ in range(height + 1)], dtype=Mark)

    for x, y in [line.split(',') for line in points]:
        page[int(y)][int(x)] = Mark('#')

    fold_order = [(axis[-1], int(val)) for axis, val in (line.split('=') for line in instructions)]
    return page, fold_order


def fold_horizontal(page, y_fold: int):
    top_half, bot_half = page[:y_fold, :], page[y_fold + 1:, :]
    for index, row in enumerate(bot_half, 1):
        top_half[-index, :] += row
    return top_half


def fold_vertical(page, x_fold: int):
    left_half, right_half = page[:, :x_fold], page[:, x_fold + 1:]
    for index, row in enumerate(right_half.T, 1):
        left_half[:, -index] += row
    return left_half


def part_1(data: list) -> int:
    page, fold_order = format_data(data)
    if fold_order[0][0] == 'x':
        page = fold_vertical(page, fold_order[0][1])
    else:
        page = fold_horizontal(page, fold_order[0][1])
    return np.count_nonzero(page == '#')


def part_2(data: list):
    page, fold_order = format_data(data)
    for fold in fold_order:
        if fold[0] == 'x':
            page = fold_vertical(page, fold[1])
        else:
            page = fold_horizontal(page, fold[1])
    for row in page:
        print(row)


if __name__ == '__main__':
    input_data = read_file_as_list('day13/input.txt')
    print(part_1(input_data))
    part_2(input_data)
