from helpers.file_manager import read_lines_with_split_as_int


def format_population(population: list) -> dict:
    return {i: x for i, x in enumerate(population)}


def simulate_fish(fishes: list, days=18) -> int:
    population = [fishes.count(i) for i in range(0, 9)]
    print('day 0: {}'.format(format_population(population)))

    for day in range(1, days + 1):
        current_breeders = population[0]
        for index in range(0, 8):
            population[index] = population[index + 1]
            if index == 7:
                population[6] += current_breeders
                population[8] = current_breeders
        print('day {}: {}'.format(day, format_population(population)))
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
