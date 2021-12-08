from helpers.file_manager import read_file_as_list


def process_data(input_data: list) -> list:
    return [line.split('|') for line in input_data]


def check_unique(reading: str):
    return len(reading) in [2, 4, 3, 7]


def get_number_from_len(reading: str):
    length = len(reading)
    if length == 2:
        return 1
    if length == 4:
        return 4
    if length == 3:
        return 7
    if length == 7:
        return 8


def part_1(input_data: list) -> int:
    return sum(sum(check_unique(x) for x in line[1].split()) for line in input_data)


def segment_mapping():
    return {
        0: ['tl', 't', 'tr', 'bl', 'b', 'br'],
        1: ['tr', 'br'],
        2: ['t', 'tr', 'm', 'bl', 'b'],
        3: ['t', 'tr', 'm', 'br', 'b'],
        4: ['tl', 'tr', 'm', 'br'],
        5: ['tl', 't', 'm', 'br', 'b'],
        6: ['tl', 't', 'm', 'bl', 'br', 'b'],
        7: ['t', 'tr','br'],
        8: ['tl', 't', 'tr', 'm', 'bl', 'br', 'b'],
        9: ['tl', 't', 'tr', 'm', 'br', 'b']
    }


def part_2(input_data: list):
    final_sum = 0
    for line in input_data:
        number_map = {int(x): 0 for x in range(0, 10)}
        digits_map = {}
        readings, digits = line
        readings = readings.split()
        for index, reading in enumerate(readings):
            if check_unique(reading):
                number_map[get_number_from_len(reading)] = reading

        digits_map['t'] = ''.join([c for c in number_map[7] if c not in number_map[1]])

        for index, reading in enumerate(readings):
            if len(reading) == 5:
                if all(c in reading for c in number_map.get(1)):
                    number_map[3] = reading
                    break

        for index, reading in enumerate(readings):
            if len(reading) == 6:
                missing = ''.join([cc for cc in number_map.get(8) if cc not in reading])
                if all(c in reading for c in number_map.get(7)):
                    if all(d in reading for d in number_map.get(3)):
                        digits_map['bl'] = missing
                        number_map[9] = reading
                    else:
                        digits_map['m'] = missing
                        number_map[0] = reading
                else:
                    digits_map['tr'] = missing
                    number_map[6] = reading

        digits_map['br'] = ''.join([c for c in number_map[1] if c is not digits_map['tr']])
        digits_map['tl'] = ''.join([c for c in number_map[4] if c not in digits_map.values()])
        digits_map['b'] = ''.join([c for c in number_map[8] if c not in digits_map.values()])

        segment_map = segment_mapping()

        output = ''
        for digit in digits.split():
            for i in range(0, 10):
                check_against = segment_map.get(i)
                final_str = ''
                for f in check_against:
                    final_str += digits_map[f]
                if all(x in digit for x in final_str) and len(digit) == len(final_str):
                    output += str(i)
                    break
        final_sum += int(output)
    return final_sum




if __name__ == "__main__":
    data = process_data(read_file_as_list('day8/input.txt'))
    print(part_1(data))
    print(part_2(data))
