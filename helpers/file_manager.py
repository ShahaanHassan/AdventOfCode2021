from pathlib import Path
import os


def get_path_too_days(file_path: str) -> str:
    days_path = Path(__file__).parent.parent
    return os.path.join(days_path, 'days', file_path)


def read_file_as_list(path: str) -> any:
    with open(get_path_too_days(path)) as file:
        return [int(i) for i in file.readlines()]

