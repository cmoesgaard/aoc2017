#!/usr/bin/python3

with open('input', 'r') as f:
    input_string = f.readline().rstrip()


def part_one():
    sum = 0
    for index, char in enumerate(input_string):
        next_index = (index + 1) % (len(input_string))
        next_char = input_string[next_index]
        if char == next_char:
            sum += int(char)
    return sum


def part_two():
    sum = 0
    input_length = len(input_string)
    for index, char in enumerate(input_string):
        next_index = (index + int(input_length / 2)) % (len(input_string))
        next_char = input_string[next_index]
        if char == next_char:
            sum += int(char)
    return sum


print("Part 1: {}".format(part_one()))
print("Part 2: {}".format(part_two()))
