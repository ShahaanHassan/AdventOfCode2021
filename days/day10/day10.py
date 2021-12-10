from helpers.file_manager import read_file_as_list


def create_brackets_map() -> dict:
    return {'(': ')', '[': ']', '{': '}', '<': '>'}


def create__score_map() -> dict:
    return {')': 3, ']': 57, '}': 1197, '>': 25137}


def create__score_map_2() -> dict:
    return {'(': 1, '[': 2, '{': 3, '<': 4}


def calculuate_score(stack: list):
    score = 0
    score_map = create__score_map_2()
    for i in reversed(stack):
        score *= 5
        score += score_map.get(i)
    return score


def check_lines(input_data: list):
    brackets_map = create_brackets_map()
    score_map = create__score_map()
    final_score = 0
    for line in input_data:
        stack = [line[0]]
        valid = True
        pos = 1
        score = 0
        while stack or pos < len(line) and valid:
            if pos > len(line)-1:
                break
            b = line[pos]
            if b not in brackets_map.values():
                stack.append(b)
            else:
                ob = stack.pop()
                if not b == brackets_map.get(ob):
                    score += score_map.get(b)
                    valid = False
            pos += 1
        if not valid:
            final_score += score
    return final_score


def check_lines_2(input_data: list):
    brackets_map = create_brackets_map()
    score_map = create__score_map()
    final_scores = []

    for line in input_data:
        stack = [line[0]]
        valid = True
        pos = 1
        while stack or pos < len(line) and valid:
            if pos > len(line)-1:
                break
            b = line[pos]
            if b not in brackets_map.values():
                stack.append(b)
            else:
                ob = stack.pop()
                if not b == brackets_map.get(ob):
                    valid = False
            pos += 1
        if valid:
            final_scores.append(calculuate_score(stack))
    a = sorted(final_scores)
    return sorted(final_scores)[len(final_scores)//2]


def part_1(input_data: list):
    print(check_lines(input_data))


def part_2(input_data: list):
    print(check_lines_2(input_data))


if __name__ == "__main__":
    input_data = read_file_as_list('day10/input.txt')
    # print(part_1(input_data))
    print(part_2(input_data))