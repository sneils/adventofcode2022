def run(data):
    elves = []
    cur = 0
    for line in data:
        if line == '\n':
            elves.append(cur)
            cur = 0
        else:
            cur += int(line.rstrip())

    elves.append(cur)
    elves.sort()

    return sum(elves[-1:]), sum(elves[-3:])
