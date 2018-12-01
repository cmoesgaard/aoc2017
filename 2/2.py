import csv

import functools

import itertools


def get_difference(string_list):
    sorted_numbers = sorted(map(int, string_list))
    return sorted_numbers[-1] - sorted_numbers[0]


def get_evenly_divisible(string_list):
    sorted_numbers = reversed(sorted(map(int, string_list)))
    for number in itertools.combinations(sorted_numbers, 2):
        modulo = number[0] % number[1]
        if modulo == 0:
            return int(number[0] / number[1])


def part_one():
    with open('input', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        return functools.reduce(lambda s, x: s + get_difference(x),
                                reader, 0)


def part_two():
    with open('input', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        return functools.reduce(lambda s, x: s + get_evenly_divisible(x),
                                reader, 0)


print("Part 1: {}".format(part_one()))
print("Part 2: {}".format(part_two()))
