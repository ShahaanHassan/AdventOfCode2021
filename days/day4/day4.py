from helpers.file_manager import read_file_as_list, read_lines_with_split_as_int
import numpy as np


def format_boards(boards: list, board_size=5) -> list:
    sanitised_rows = [list(map(lambda x: int(x), line.split())) for line in boards if line != '']
    return list(np.array([sanitised_rows[i:i+board_size] for i in range(0, len(sanitised_rows), board_size)]))


def check_for_winning_rows(rolls: list, board) -> bool:
    return any(all(entry in rolls for entry in row) for row in board)


def check_for_winning_columns(rolls: list, board, board_size=5) -> bool:
    return any(all(entry in rolls for entry in board[:, col]) for col in range(0, board_size))


def get_answer(rolls: list, board) -> int:
    return sum(x for row in board for x in row if x not in rolls) * rolls[-1]


def check_for_winning_board(checked_rolls: list, board) -> bool:
    return check_for_winning_rows(checked_rolls, board) or check_for_winning_columns(checked_rolls, board)


def part_1(rolls: list, boards: list) -> int:
    boards = format_boards(boards)
    for i in range(5, len(rolls)):
        checked_rolls = rolls[:i]
        for board in boards:
            if check_for_winning_board(checked_rolls, board):
                return get_answer(checked_rolls, board)


def part_2(rolls: list, boards: list) -> int:
    boards = format_boards(boards)
    remaining_boards = boards.copy()
    for i in range(5, len(rolls)):
        checked_rolls = rolls[:i]
        if len(remaining_boards) == 1:
            return get_answer(checked_rolls, remaining_boards[0])
        for index, board in enumerate(boards):
            if check_for_winning_board(checked_rolls, board):
                del remaining_boards[index]
        boards = remaining_boards


if __name__ == "__main__":
    roll_data = read_lines_with_split_as_int('day4/input_rolls.txt')
    board_data = read_file_as_list('day4/input_boards.txt')
    print(part_1(roll_data, board_data))
    print(part_2(roll_data, board_data))
