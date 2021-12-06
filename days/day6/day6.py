from helpers.file_manager import read_lines_with_split_as_int


def simulate_fish(fishes: list, days=18) -> int:
    population = [fishes.count(i) for i in range(0, 9)]
    print('day 0: {}'.format(population))

    for day in range(1, days + 1):
        new_population = [0] * 9
        for index in range(8, 0, -1):
            if index == 1:
                new_population[6] += population[0]
                new_population[8] = population[0]
            new_population[index - 1] = population[index]
        population = new_population
        print('day {}: {}'.format(day, {i: x for i, x in enumerate(population)}))
    return sum(population)


def part_1(input_data: list):
    print('part 1')
    print('total fish: {}'.format(simulate_fish(input_data, 80)))
    print()


def part_2(input_data: list):
    print('part 2')
    print('total fish: {}'.format(simulate_fish(input_data, 256)))
    print()


if __name__ == "__main__":
    data = read_lines_with_split_as_int('day6/input.txt')
    part_1(data)
    part_2(data)
