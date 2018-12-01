def part_one():
    with open('input', 'r') as f:
        words = map(lambda x: x.split(), f)
        return len(list(filter(lambda x: len(x) == len(set(x)), words)))


def part_two():
    with open('input', 'r') as f:
        sorted_words = map(lambda x: list(map(lambda y: "".join(sorted(y)), x.split())), f)
        valid_phrases = filter(lambda x: len(x) == len(set(x)), sorted_words)
        return len(list(valid_phrases))


print("Part 1: {}".format(part_one()))
print("Part 2: {}".format(part_two()))
