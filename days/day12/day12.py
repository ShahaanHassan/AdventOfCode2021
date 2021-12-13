from collections import defaultdict

from helpers.file_manager import read_file_as_list


def create_graph(data: list) -> dict:
    graph = defaultdict(list)

    for line in data:
        start, end = line.split('-')
        if end != 'start':
            graph[start].append(end)
        if start != 'start':
            graph[end].append(start)
    return graph


def find_paths(graph: dict, current: str, visited: list, doubles: dict, count_double=False):
    if current == 'end':
        return 1

    total = 0
    if count_double and current.islower() and current not in ['start', 'end']:
        doubles[current] = doubles.get(current, 0) + 1

    for n in graph[current]:
        can_double = count_double and list(doubles.values()).count(2) < 1
        if n.isupper() or can_double or n not in visited:
            total += find_paths(graph, n, visited + [current], dict(doubles), count_double)
    return total


def part_1(data: list):
    graph = create_graph(data)
    return find_paths(graph, 'start', [], {})


def part_2(data: list):
    graph = create_graph(data)
    return find_paths(graph, 'start', [], {}, True)


if __name__ == "__main__":
    input_data = read_file_as_list('day12/input.txt')
    print(part_1(input_data))
    print(part_2(input_data))
