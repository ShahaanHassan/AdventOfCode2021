from helpers.file_manager import read_file_as_list


def create_brackets_map() -> dict:
    return {'(': ')', '[': ']', '{': '}', '<': '>'}


def create_score_map() -> dict:
    return {')': 3, ']': 57, '}': 1197, '>': 25137}


def create_score_map_2() -> dict:
    return {'(': 1, '[': 2, '{': 3, '<': 4}


def calculate_score(stack: list):
    score = 0
    score_map = create_score_map_2()
    for i in reversed(stack):
        score = (score * 5) + score_map.get(i)
    return score


def check_line(line: list, stack: list, score_map: dict, brackets_map: dict, part: int):
    if not line:
        return 0 if part == 1 else calculate_score(stack)

    cb = line.pop(0)
    if cb not in brackets_map.values():
        stack.append(cb)
    else:
        ob = stack.pop()
        if not cb == brackets_map.get(ob):
            return score_map.get(cb) if part == 1 else 0
    return check_line(line, stack, score_map, brackets_map, part)


def part_1(lines: list, score_map=create_score_map) -> int:
    brackets_map, score_map = create_brackets_map(), score_map()
    score = 0
    for line in lines:
        score += check_line(list(line)[1:], [line[0]], score_map, brackets_map, 1)
    return score


def part_2(lines: list, score_map=create_score_map_2) -> int:
    brackets_map, score_map = create_brackets_map(), score_map()
    scores = [check_line(list(line)[1:], [line[0]], score_map, brackets_map, 2) for line in lines]
    final_scores = list(filter(lambda x: x != 0, scores))
    return sorted(final_scores)[len(final_scores) // 2]


if __name__ == "__main__":
    data = read_file_as_list('day10/input.txt')
    print(part_1(data))
    print(part_2(data))
