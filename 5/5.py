def get_offsets():
    with open('input', 'r') as f:
        return [int(line) for line in f.readlines()]


def part_one():
    offsets = get_offsets()
    length = len(offsets)
    index = 0
    steps = 0
    while index < length:
        old_index = index
        index += offsets[index]
        offsets[old_index] += 1
        steps += 1
    return steps


def part_two():
    offsets = get_offsets()
    length = len(offsets)
    index = 0
    steps = 0
    while index < length:
        old_index = index
        index += offsets[index]
        if offsets[old_index] >= 3:
            offsets[old_index] -= 1
        else:
            offsets[old_index] += 1
        steps += 1
    return steps


print('Part 1: {}'.format(part_one()))
print('Part 2: {}'.format(part_two()))
