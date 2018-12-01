import math

steps = []
with open('input', 'r') as f:
    directions = f.read().rstrip().split(',')
    x, y, z = 0, 0, 0
    for dir in directions:
        if dir == 'nw':
            x += 1
            y -= 1
        elif dir == 'n':
            y -= 1
            z += 1
        elif dir == 'ne':
            x -= 1
            z += 1
        elif dir == 'se':
            x -= 1
            y += 1
        elif dir == 's':
            y += 1
            z -= 1
        elif dir == 'sw':
            x += 1
            z -= 1
        steps.append((x, y, z))


def calc_distance(step):
    return int((math.fabs(step[0]) + math.fabs(step[1]) + math.fabs(step[2])) / 2)


def part_one():
    return calc_distance(steps[-1])


def part_two():
    return max(map(calc_distance, steps))


print("Part 1: {}".format(part_one()))
print("Part 2: {}".format(part_two()))
