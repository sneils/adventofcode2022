def parse_elf(s):
    a, b = s.split("-")
    return [*range(int(a), int(b)+1)]


def run(data):
    part1, part2 = 0, 0

    for line in data:
        elf1, elf2 = (parse_elf(elf) for elf in line.rstrip().split(","))

        if any(x in elf1 for x in elf2):
            part2 += 1
            if all(x in elf1 for x in elf2) or all(x in elf2 for x in elf1):
                part1 += 1

    return part1, part2
