from pathlib import Path
import os


def get_path_to_days(file_path: str) -> str:
    root_path = Path(__file__).parent.parent
    return os.path.join(root_path, 'days', file_path)


def read_file_as_list(path: str) -> list:
    with open(get_path_to_days(path)) as file:
        return [i.rstrip() for i in file.readlines()]


def read_file_as_int_list(path: str) -> list:
    with open(get_path_to_days(path)) as file:
        return [int(i) for i in file.readlines()]


def read_lines_with_split_as_int(path: str, split=',') -> list:
    with open(get_path_to_days(path)) as file:
        return [int(i) for i in file.readline().split(split)]
