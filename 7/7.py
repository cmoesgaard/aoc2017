def part_one():
    keys = set()
    values = set()

    with open('input', 'r') as f:
        for line in f.readlines():
            split_string = line.rstrip().replace(',', '').split(' ')
            keys.add(split_string[0])
            values.update(split_string[3:])

    return keys.difference(values)


def part_two():
    weights = {}
    subs = []
    with open('input', 'r') as f:
        for line in f.readlines():
            split_string = line.rstrip().replace(',', '').replace('(', '').replace(')', '').split(' ')
            weights[split_string[0]] = split_string[1]
            if len(split_string) > 2:
                subs.append(split_string[3:])

    for sub in subs:
        sum = 0
        for el in sub:
            sum += int(weights[el])
        print(sum/len(sub))


print("Part 1: {}".format(part_one()))
print("Part 2: {}".format(part_two()))
