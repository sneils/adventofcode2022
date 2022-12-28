from itertools import product, islice
from string import ascii_letters


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def run(data):
    rucksacks = []
    for line in data:
        l = len(line) // 2
        rucksacks.append((line[:l], line[l:]))

    in_both = list()
    for (a, b) in rucksacks:
        in_both += set(x for (x, y) in product(set(a), set(b)) if x == y)

    part1 = sum([ascii_letters.index(c) + 1 for c in in_both])
    part2 = 0

    for group in chunk(rucksacks, 3):
        items = [a + b for (a, b) in group]
        for item in items[0]:
            if item in items[1] and item in items[2]:
                part2 += ascii_letters.index(item) + 1
                break

    return part1, part2
